class BankAccount:
    def __init__(self, tentk, stk, so_du=50):
        self.ten_tai_khoan = tentk
        self.so_tai_khoan = stk
        self._so_du = so_du

    def nap_tien(self, so_tien):
        'make deposit'
        if so_tien <=0:
            raise ValueError ('So tien nap khong hop le')
        else:
            self._so_du += so_tien

    def rut_tien (self, so_tien):
        'make widthdraw'
        if so_tien > self.so_du:
            raise ValueError ('Tai khong khong du tien de thuc hien giao dich')
        else:
            self._so_du -= so_tien

    @property
    def so_du(self):
        'check balance'
        return self._so_du

    def __str__(self):
        return (f'\
            So tai khoan: {self.so_tai_khoan}  \n\
            Ten tai khoan: {self.ten_tai_khoan} \n\
            So du: ${self._so_du}')

    def chuyen_khoan(self, so_tien, func):
        if so_tien > 0:
            self.rut_tien(so_tien)
            func(so_tien)
        else:
            pass

customer1 = BankAccount('Alex', '19005858')
customer1.nap_tien(100)
customer1.rut_tien(30)
print(customer1.__str__())

customer2 = BankAccount('Tom', '19005151', 10)


so_tien_chuyen = int(input('Nhap so tien chuyen: '))
customer1.chuyen_khoan(so_tien_chuyen,customer2.nap_tien)

print('--------------')
print(f'So du con lai: {customer1.so_du}')
print(f'So du tai khoan nguoi nhan: {customer2.so_du}')
