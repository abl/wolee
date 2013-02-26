import fileinput, logging, re

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)-8s] %(message)s')
log = logging.getLogger()

try:
    import ujson as json
except ImportError:
    log.warning("Unable to load ujson, defaulting to json")
    import json

combat = None
timing = None

detect_combat = re.compile("^\s+combatLog = (.*)")
detect_timing = re.compile("^\s+resultTimeRanges = (.*)")

previous_file = None

c = None
t = None

#Combat keys:
#flaggedActors
#spells
#actors
#events
#entries ()

def process(combat, timing):
    global c,t
    c = combat
    t = timing

for line in fileinput.input():
    if fileinput.isfirstline():
        if combat is not None or timing is not None:
            log.warning("Did not find combat and timing information in file %s" % previous_file)
        combat = None
        timing = None
        previous_file = fileinput.filename()
        
    if combat is None:
        m = detect_combat.match(line)
        if m:
            combat = json.loads(m.group(1))
    else:
        m = detect_timing.match(line)
        if m:
            timing = json.loads(m.group(1))
            process(combat, timing)
            combat = None
            timing = None
            fileinput.nextfile()

if combat is not None or timing is not None:
    log.warning("Did not find combat and timing information in file %s" % previous_file)  