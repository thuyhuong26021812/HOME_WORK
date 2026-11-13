# Viết chương trình nhập vào 1 số nguyên dương n. Tính tổng những số chia hết cho 3 hoặc 5 từ 1 đến n

n =  int(input())
tong = 0
for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0:
        tong+=i
print(tong)