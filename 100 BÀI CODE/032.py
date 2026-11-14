# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Đếm xem trong các số nguyên từ m đến n, có bao nhiêu số chia hết cho 3 hoặc chia hết cho 5. Tính tổng các số chẵn.

m, n = map( int, input().split())
a = []
tong = 0
for i in range(m,n+1):
    if i % 3 == 0 or i % 5 == 0:
        a.append(i)
    if i % 2 == 0:
        tong += i
print(len(a), tong)
