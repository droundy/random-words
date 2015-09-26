print """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array
        name="words">"""

with open("google-10000-english-usa.txt", 'r') as content_file:
    google = content_file.read().split();
with open("/usr/share/dict/american-english-small", 'r') as content_file:
    usr_share = content_file.read().split();

words = [val for val in google if val in usr_share]
words.sort()

def is_bad(s, last):
    return "'" in s or s == last + "s" or s == last + "ed" or s == last + "ing" or len(s) == 1 or s == last + "ly"

new = []
last = ""
for i in words:
    if not is_bad(i, last):
        new.append(i)
        last = i

words = [val for val in google if val in new]

for i in words:
    print("""        <item>%s</item>""" % i)
    last = i

print """    </string-array>
</resources>
"""
