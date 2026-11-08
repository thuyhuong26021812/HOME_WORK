# Bài 2: Nhập vào bán kính của hình tròn. In ra màn hình diện tích và chu vi của nó.  

import math
n = float(input('Bán kính hình tròn: '))
dien_tich = math.pi * (n**2)
chu_vi = 2*n*math.pi
print('Diện tích hình tròn: ',dien_tich, '\nChu vi hình tròn: ', chu_vi )