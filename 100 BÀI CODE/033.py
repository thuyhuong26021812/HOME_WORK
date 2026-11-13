# Viết chương trình nhập vào 2 số nguyên m và n (m<n). Đếm xem trong các số nguyên từ m đến n, có bao nhiêu số nguyên tố

n, m = map(int, input().split())
a = []
for i in range(m, n+1):
    for x in range(m, n+1):
        if x%i==0:
            x.append(a)
if len(a) == 2:
    