# Bài 5: Viết chương trình giải phương trình bậc 2 (ax2 + bx + c = 0)

import math
a = float(input('nhap he so: '))
b = float(input('nhap he so: '))
c = float(input('nhap he so: '))
delta = b**2 - 4*a*c
print(f'phuong trinh bac 2: {a}*x^2 + {b}*x + {c} = 0')
if delta == 0:
    print('phuong trinh co nghiem duy nhat: x = ', -b/2*a)
elif delta > 0:
    print('phuong trinh co 2 nghiem phan biet:','\nx1 = ', (-b + math.sqrt(delta))/2*a, '\nx2 = ',(-b - math.sqrt(delta))/2*a)
elif delta < 0:
    print('phuong trinh vo nghiem')