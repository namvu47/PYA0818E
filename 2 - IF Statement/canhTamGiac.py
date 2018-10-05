print('Nhap 3 so nguyen duong bat ky \n')

_a = int(input("Nhap so thu nhat: "))
_b = int(input("Nhap so thu hai: "))
_c = int(input("Nhap so thu ba: "))

if (_a+_b>_c) and (_a+_c>_b) and (_b+_c>_a):
    print('3 so ban vua nhap la 3 canh tam giac!')
else:
    print ('3 so ban vua nhap KHONG la 3 canh tam giac!')
