# Viết chương trình kiểm tra xem 3 số a, b, c nhập từ bàn phím có là 3 cạnh của một tam giác hay ko? Nếu phải thì tính chu vi và diện tích của tam giác đó, ngược lại thông báo 3 số đó ko phải là 3 cạnh của tam giác

import math
a, b, c = map(int, input().split())
if min(a,b,c) > 0 and a+b>c and a+c>b and b+c>a:
    p = (a+b+c)/2
    cv = 2*p
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Day là 3 canh cua mot tam giac', f'\n{cv:.2f}  {s:.1f}')
else:
    print('Day khong phai la 3 canh cua mot tam giac')