#! python
import pprint
message = 'one two three four five six seven eight nine ten'
count = {}

for letter in message:
        count.setdefault(letter ,0)
        count[letter] += 1

pprint.pprint(count)
