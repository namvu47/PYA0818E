# return dic from string: key - character : value - number of appearance

_strInput = str(input('Nhap vao 1 chuoi: \n'))

_dict = {}

for i in _strInput:
    _dict[i] = _dict.get(i, 0) + 1

print (_dict)