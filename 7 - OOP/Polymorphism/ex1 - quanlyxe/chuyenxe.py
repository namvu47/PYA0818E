class chuyenxe:
    def __init__(self, ma, tx,sx, dt):
        self.ma_xe = ma
        self.ten_tx = tx
        self.so_xe = sx
        self.doanh_thu = dt

    def __str__(self):
        return (f'\
        - Ma chuyen xe: {self.ma_xe} \n\
        - Ten lai xe: {self.ten_tx} \n\
        - So xe: {self.so_xe} \n\
        - Doanh thu: {self.doanh_thu}')


