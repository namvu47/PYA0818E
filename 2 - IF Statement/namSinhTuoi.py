import time

_namsinh = int(input('Nhap nam sinh cua ban: '))

_year = (time.localtime())[0]

print('So tuoi cua ban la: ', _year - _namsinh)
