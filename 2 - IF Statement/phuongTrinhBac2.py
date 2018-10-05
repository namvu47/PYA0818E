import math

print("*** Chuong trinh sau giai phuong trinh bac hai ax^2+bx+c = 0 *** \n")

_a = int (input("Nhap a: "))
_b = int (input("Nhap b: "))
_c = int (input("Nhap c: "))

_delta = (_b**2 - 4*_a*_c)

if _a != 0:

    if _delta <0:
        print(f'Phuong trinh {_a}x^2+{_b}x+{_c} = 0 vo nghiem')

    elif _delta == 0:
        print(f'Phuong trinh {_a}x^2 + {_b}x +{_c} = 0 co 1 nghiem duy nhat: ')
        print ("x = {0:.2f}".format (-_b / (2*_a)))
    else:
        print(f'Phuong trinh {_a}x^2+{_b}x{_c} = 0 co 2 nghiem: ')
        print ("x1 = {0:.2f}".format ((-_b+ math.sqrt(_delta)) / (2*_a)))
        print("x2 = {0:.2f}".format ((-_b - math.sqrt(_delta)) / (2 * _a)))


else:
    if (_b == 0) and (_c == 0):
        print(f'Phuong trinh {_a}x^2 + {_b}x +{_c} = 0 dung voi moi x!!!')
    elif (_b == 0) and (_c != 0):
        print(f'Phuong trinh {_a}x^2 + {_b}x +{_c} = 0 vo nghiem!!! ')
    else:
        print(f"Phuong trinh {_b}x+{_c} = 0 co 1 nghiem duy nhat: \n")
        print(f"x = {(-_c / _b):.2f}")
