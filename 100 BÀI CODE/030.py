# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Tính tổng các số nguyên từ m đến n

m, n = map(int, input().split())
tong = 0
for i in range(m,n+1):
    tong += i
print(tong)