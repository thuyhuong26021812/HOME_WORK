# Viết chương trình tính trung bình cộng của 3 số nguyên a, b, c theo công thức TBC=(a+b+c)/3

a, b, c = map(int, input().split())
tbc = (a+b+c)/3
print(f'{tbc:.1f}')