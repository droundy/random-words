import urllib2, re, subprocess

wikitop = re.findall(r'>([^<]+)</a></td>',
                     urllib2.urlopen("http://stats.grok.se/en/top").read())

things_to_avoid = [':', '?', 'List of ', 'xxx', 'XXX', '/', '.html',
                   '201', ' (season ', 'Main Page', '404 error']
for t in things_to_avoid:
    wikitop = [x for x in wikitop if not t in x]
wikitop = [t.replace('&#39;', r"\'") for t in wikitop]
wikitop = [t.replace('&amp;', "and") for t in wikitop]
redundant = wikitop
wikitop = []
for x in redundant:
    if not x in wikitop:
        wikitop.append(x)

with open("google-10000-english-usa.txt", 'r') as content_file:
    google = content_file.read().split();
with open("/usr/share/dict/american-english-small", 'r') as content_file:
    usr_share = content_file.read().split();

def is_noun_or_etc(w):
    try:
        definition = subprocess.check_output(["dict","-f",'-C',"-d","wn",w])
        return ' n ' in definition or ' v ' in definition or ' adj ' in definition
    except:
        return False

words = [val for val in google if val in usr_share and is_noun_or_etc(val)]

def is_okay(w):
    return not "'" in w

words = filter(is_okay, words)

print """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array
        name="words">"""

for i in wikitop + words[:500]:
    print("""        <item>%s</item>""" % i)

print """    </string-array>
    <string-array
        name="wikipedia">"""

for i in wikitop:
    print("""        <item>%s</item>""" % i)

print """    </string-array>
    <string-array
        name="manywords">"""

for i in words:
    print("""        <item>%s</item>""" % i)

print """    </string-array>
</resources>
"""
