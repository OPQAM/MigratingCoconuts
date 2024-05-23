#!/usr/bin/env python3

spam = {'dick': 'Barry', 'number': 2}

for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for k, v in spam.items():
    print(f"key: {k}; value: {v}")

print(str(spam.get('number', 0)))

maps = {'benny': ['0000', '1111', '2222', '3333', '4444', '5555']}

print(str(maps.get('benny', 'bulldog')))

'''So, basically, the second value (here bulldog) is a fallback value, in case the key we're asking for doesn't exists. If it does, we get the respective value'''


'''setdefault() method'''

if 'portugal' not in maps:
    maps['portugal'] = 'country'

print(maps)