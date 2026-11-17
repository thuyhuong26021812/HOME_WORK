# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Tính trung bình cộng các số nguyên tố từ m đến n.  Nếu không có số nào thì in dấu - 

m, n = map(int, input().split())
tong = 0
a = []
for i in range(m, n+1):
    b = []
    for j in range(1, n+1): 
        if i%j==0:
            b.append(j)
    if len(b)==2:
        a.append(i)
        tong += i
c = len(a)
print(f'{tong/c:.2f}')
