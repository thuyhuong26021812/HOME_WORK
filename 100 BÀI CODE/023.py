# Viết chương trình nhập vào 1 số nguyên dương n. In ra những số chia hết cho 3 trong các số từ 1 đến n, nếu không có số nào thì in -.

n = int(input()) 
for i in range(1,n+1):
    if i % 3 == 0 and i != 0:
        print(i, end=' ') 
