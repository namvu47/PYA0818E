_a = int (input('Nhap 1 so nguyen duong bat ky: '))

if _a % 2 == 0:
    if _a % 3 == 0:
        print ("So ban vua nhap chia het cho ca 2 va 3!")
    else:
        print("So ban vua nhap chia het cho 2 nhung khong chia het cho 3!")
else:
    if _a % 3 != 0:
        print ("So ban vua nhap khong chia het cho ca 2 va 3!")
    else:
        print("So ban vua nhap chia het cho 3 nhung khong chia het cho 2!")