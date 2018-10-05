from Polymorphism.ex2.sachthamkhao import *
from Polymorphism.ex2.sachgiaokhoa import *

# print('---------------------------------------------------------')
# print('Nhap thong tin sach giao khoa: (Ma sach, Ngay Nhap, Don gia, So Luong, Nha Xuat Ban, Tinh Trang) \n')
# numberofsgk = int(input("Nhap so luong dau sach giao khoa: "))
# for x in range(1, numberofsgk+1):
#     globals()[f'dausachgk{x}'] = input(f"Thong tin sach giao khoa {x}: ").split(',')
#     print ((sachgiaokhoa(*globals()[f'dausachgk{x}'])).__str__())
#     print(f'Tong tien loai {x}: ' + (sachgiaokhoa(*globals()[f'dausachgk{x}'])).thanhtien())


print('---------------------------------------------------------')
print('Nhap thong tin sach tham khao: (Ma sach, Ngay Nhap, Don gia, So Luong, Nha Xuat Ban, Thue) \n')
numberofstk = int(input("Nhap so luong dau sach tham khao: "))
sumstk = 0
for x in range(1, numberofstk+1):
    globals()[f'dausachtk{x}'] = input(f"Thong tin sach tham khao {x}: ").split(',')
    print ((sachthamkhao(*globals()[f'dausachtk{x}'])).__str__())
    print(f'Tong tien loai {x}: ' + (sachthamkhao(*globals()[f'dausachtk{x}'])).thanhtien())
    sumstk += int((globals()[f'dausachtk{x}'])[2])
print ('Trung binh cong don gia cua sach tham khao: ', sumstk/numberofstk)




