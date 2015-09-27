import urllib2, re

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

words = [val for val in google if val in usr_share]

def is_okay(w):
    return not "'" in w

words = filter(is_okay, words)

for w in usr_share:
    if w + 's' in words:
        words.remove(w + 's')
    if w + 'ing' in words:
        words.remove(w + 'ing')
    if w + 'ed' in words:
        words.remove(w + 'ed')
    if w + 'ly' in words:
        words.remove(w + 'ly')
    if w[-1] == 'y' and w[:-1] + 'ily' in words:
        words.remove(w[:-1] + 'ily')
    if w[-1] == 'e':
        if w[:-1] + 'ing' in words:
            words.remove(w[:-1] + 'ing')
        if w[:-1] + 'ed' in words:
            words.remove(w[:-1] + 'ed')
    if w[-1] == 'm':
        if w + 'ming' in words:
            words.remove(w + 'ming')
        if w + 'med' in words:
            words.remove(w + 'med')


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
