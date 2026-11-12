# Viết chương trình tính chu vi (cv) và diện tích (s) một tam giác có 3 cạnh a, b, c là các số nguyên theo công thức cv=a+b+c, s=sqrt(p*(p-a)*(p-b)*(p-c)) với p=cv/2 (3 số a, b, c bảo đảm là 3 cạnh của 1 tam giác)

import math
a, b ,c = map(int, input().split())
cv = a+b+c
p = cv/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'{cv:.1f}, {s:.3f}')