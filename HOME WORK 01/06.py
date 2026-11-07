import math
a, b , c = map(int, input().split())
p = (a + b + c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
if min(a, b, c)>0 and a + b > c and a + c > b and b + c > a:
    print('Dien tich:', f'{s:.1f}')
else:
    print('Khong phai 3 cạnh cua tam giap')
    