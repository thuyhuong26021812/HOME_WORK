# Viết chương trình tính diện tích tam giác có chiều dài cạnh đáy a và chiều cao h tương ứng là các số nguyên theo công thức s=a*h/2

a, h = map(int, input().split())
s = a*h/2
print(f'{s:.2f}')