# Viết chương trình nhập vào 1 số nguyên dương n. Đếm xem n có bao nhiêu ước

n = int(input())
m=[]
for i in range(1,n+1):
    if n % i == 0:
        m.append(i)
print(len(m))