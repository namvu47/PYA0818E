from Polymorphism.ex1.chuyenxe import *

class xenoithanh(chuyenxe):
    def __init__(self,ma, tx, sx, dt, so_km, so_tuyen):
        super().__init__(self,ma,tx,sx,dt)
        self.__so_km = so_km
        self.__so_tuyen = so_tuyen

    def __str__(self):
        return chuyenxe.__str__(self) + (f'\n\
        - So Km: {self.__so_km} \n\
        - So tuyen: {self.__so_tuyen} ')