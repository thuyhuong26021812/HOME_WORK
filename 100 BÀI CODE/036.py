# Tìm UCLN của 2 số nguyên dương a, b

a, b = map(int, input().split())
m = []
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        m.append(i)
print(max(m))