#Viết chương trình nhập vào 2 số nguyên m và n (m<n). Đếm xem trong các số nguyên từ m đến n, có bao nhiêu số chia hết cho 3

m, n = map(int, input().split())
a = []
for i in range(m,n+1):
    if i%3==0:
        a.append(i)
print(len(a))