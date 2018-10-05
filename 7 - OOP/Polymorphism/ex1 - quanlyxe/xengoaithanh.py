from Polymorphism.ex1.chuyenxe import *

class xengoaithanh(chuyenxe):
    def __init__(self,ma, tx, sx, dt, noi_den, so_ngay):
        super().__init__(self,ma,tx,sx,dt)
        self.__noi_den = noi_den
        self.__so_ngay = so_ngay

    def __str__(self):
        return chuyenxe.__str__(self) + (f' \n\
        - Noi den: {self.__noi_den} \n\
        - So ngay: {self.__so_ngay} ')
