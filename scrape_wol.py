import httplib2, time, os, sys

#By default, here's a random Garalon attempt.
URI = "http://www.worldoflogs.com/reports/nudzscuaxonmp7l7/xe/?enc=bosses&boss=63667&x=((type%3DTYPE_DAMAGE)+and+targetType%3D%22Player%22+and+(targetId%3D141+or+targetId%3D5))+or+(fullType%3DSPELL_AURA_APPLIED_DOSE+and+spell%3D%22Pungency%22)&page="

if len(sys.argv) > 1:
    URI = sys.argv[1]

import httplib2
h = httplib2.Http(".cache")

if not os.path.exists("tmp"):
    os.mkdir("tmp")

for x in range(50):
    print "Loading page %02d..." % x,
    resp, content = h.request(URI+str(x))
    with open("tmp/wol-page-%02d.html" % x, 'w') as f:
        f.write(content)
    print "done!"