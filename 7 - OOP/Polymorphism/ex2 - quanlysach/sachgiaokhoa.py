from Polymorphism.ex2.sach import *

class sachgiaokhoa(sach):
    def __init__(self, masach, ngaynhap, dongia, soluong, nhaxuatban, tinhtrang):
        super().__init__(masach, ngaynhap,dongia,soluong,nhaxuatban)
        self.tinh_trang = tinhtrang

    def thanhtien(self):
        tiensachgiaokhoa = 0
        if self.tinh_trang.replace(' ','') == 'moi':
            tiensachgiaokhoa += int(self.so_luong) * int(self.don_gia)
        else:
            tiensachgiaokhoa += int(self.so_luong) * int(self.don_gia) * 0.5
        return f'{tiensachgiaokhoa:0.2f}'


    def __str__(self):
        return sach.__str__(self) + (f' \n\
        6. Tinh trang: {self.tinh_trang} ')


