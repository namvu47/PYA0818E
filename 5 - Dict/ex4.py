_dict = {'4': 's001', '5': 's002', '6': 's001', '7': 's005', '8':'s005', '9': 's009', '10': 's007'}
_l = []

for i in _dict:
    _l.append(_dict[i])

print (set(_l))

# set(list): return unique element in a list