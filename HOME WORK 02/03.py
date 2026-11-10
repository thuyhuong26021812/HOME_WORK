# Bài 3 : Tính tam giác: Nhâp vào ba số a,b,c bất kì. Kiểm tra xem nó có thể là độ dài ba cạnh hay không, nếu  không thì in  ra màn  hình  'Khong la ba  canh cua mot tam  giac'. Ngược lại, kiểm tra xem nó là tam giác gì: Đều, Cân, Vuông, hay Tam giác thường. Tính diện tích, chu vi của tam giác và in ra màn hình. 

import math
a, b, c = map(float, input('độ dài 3 cạnh: ').split())
if min(a,b,c)>0 and a+b>c and a+c>b and b+c>a:
    p = a + b + c # chu vi
    s = math.sqrt(p/2*(p/2-a)*(p/2-b)*(p/2-c))
    if a==b or a==c or b==c:
        print('Tam giac can', '\nChu vi: ',p, '\nDiện tích: ',s) 
    elif a==b==c:
        print('Tam giac deu', '\nChu vi: ',p, '\nDiện tích: ',s)
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('Tam giac vuong', '\nChu vi: ',p, '\nDiện tích: ',s)
    else:
        print('Tam giac thuong','\nChu vi: ',p, '\nDiện tích: ',s)
else:
    print('Khong la canh cua mot tam giac')