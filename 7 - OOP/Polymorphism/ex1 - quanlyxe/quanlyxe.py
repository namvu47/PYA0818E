xenoithanh = input('Nhap xe noi thanh: \n' )
xengoaithanh = input('Nhap xe ngoai thanh: \n')

listnoithanh = xenoithanh.split(',')
listngoaithanh = xengoaithanh.split(',')

from Polymorphism.ex1.xengoaithanh import *
from Polymorphism.ex1.xenoithanh import *

xent = xenoithanh(*listnoithanh)
xengt = xengoaithanh(*listngoaithanh)

print(xent.__str__())
print(xengt.__str__())

