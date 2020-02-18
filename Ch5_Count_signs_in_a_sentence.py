

import pprint

message = 'Phyton blablablablabla appppppp'
count = {}

for char in message:
    count.setdefault(char,0)
    count[char] += 1

pprint.pprint(count)
(pprint.pformat(count))

