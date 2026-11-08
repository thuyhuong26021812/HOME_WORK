# Bài 10: Nhập vào tâm và bán kính của một đường tròn. Sau đó nhập vào một điểm A(x, y) bất kì và kiểm tra xem nó có thuộc đường tròn hay không?

import math
x, y = map(float, input().split())
print(f'toa do tam I({x},{y})')
n = float(input('ban kinh: '))
a, b = map(float, input().split())
print(f'toa do diem A({a},{b})')
khoang_cach = math.sqrt((x-a)**2 + (y-b)**2)
print('Do dai IA = ',khoang_cach)
if khoang_cach <= n:
    print('Diem A thuoc duong tron')
elif khoang_cach > n:
    print('Diem A khong thuoc duong tron')