# check if input matches key, return value

_dict = {'4': 's001', '5': 's002', '6': 's001', '7': 's005', '8':'s005', '9': 's009', '10': 's007'}

_input = str(input ('Nhap key: \n'))

for i in _dict:
    if _input == i:
        print (f'Value tuong ung trong dict: {_dict[i]}')
    else:
        pass
