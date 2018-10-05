class sach:
    def __init__(self, masach, ngaynhap, dongia, soluong, nhaxuatban):
        self.ma_sach = masach
        self.ngay_nhap = ngaynhap
        self.don_gia = dongia
        self.so_luong = soluong
        self.nhaxuatban = nhaxuatban

    def __str__(self):
        return (f'\
        1. Ma sach: {self.ma_sach} \n\
        2. Ngay nhap: {self.ngay_nhap} \n\
        3. Don gia: {self.don_gia} \n\
        4. So luong: {self.so_luong} \n\
        5. Nha xuat ban: {self.nhaxuatban} ')

