from Polymorphism.ex2.sach import *

class sachthamkhao(sach):
    def __init__(self,masach, ngaynhap, dongia, soluong, nhaxuatban, thue):
        super().__init__(masach, ngaynhap,dongia,soluong,nhaxuatban)
        self.thue = thue

    def thanhtien(self):
        tiensachthamkhao = int(self.so_luong) * int(self.don_gia) * (1+int(self.thue)/100)
        return f'{tiensachthamkhao:0.2f}'

    def __str__(self):
        return sach.__str__(self) + (f' \n\
        6. Thue: {self.thue}% ')

