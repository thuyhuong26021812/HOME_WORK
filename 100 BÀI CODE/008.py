# Viết chương trình tính bán kính R của đường tròn ngoại tiếp tam giác có ba cạnh a,b,c là các số nguyên theo công thức R= abc/4S đảm là 3 cạnh của 1 tam giác), với S là diện tích tam giác (3 số a, b, c bảo

import math
a, b, c = map(int, input().split())
if min(a,b,c) > 0 and a+b>c and a+c>b and b+c>a:
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    r = (a*b*c)/(4*s)
    print(f'{r:.3f}')