# 5.So sánh 2 số: Viết chương trình nhập vào hai số, in ra số lớn hơn hoặc thông báo nếu hai số bằng nhau. 

n = float(input())
m = float(input())
if n==m:
    print ('Hai số bằng nhau')
elif m != n:
    print(max(m,n))