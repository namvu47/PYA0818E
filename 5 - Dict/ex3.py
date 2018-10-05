#combine 2 dict when key is the same

d1 = {'a': 15, 'b': 20, 'c': 30, 'e': 60}
d2 = {'a': 30, 'b': 25, 'd':50}

for key2, value2 in d2.items():
    if key2 in d1:
        d1[key2] += value2
    else:
        d1[key2] = value2

print(f'New dic: {d1}')

