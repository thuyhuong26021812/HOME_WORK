# Viết chương trình nhập vào 1 số nguyên dương n. Tính tổng những số chẵn từ 1 đến n.

n = int(input())
tong = 0
for i in range(1,n+1):
    if i % 2 == 0:
        tong += i
print(tong)