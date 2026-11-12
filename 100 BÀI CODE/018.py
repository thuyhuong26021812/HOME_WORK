# Viết chương trình nhập vào 1 tháng và năm, cho biết tháng đó có bao nhiêu ngày (Năm nhuận là năm chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100).

m, ys = map(int, input().split())
if ys % 4 == 0 or (ys % 4 == 0  and ys % 100 != 0):
    if m in (1,3,5,7,8,10,12):
        print('31')
    elif m == 2:
        print('29')
    else:
        print('30')
else:
    if m in (1,3,5,7,8,10,12):
        print('31')
    elif m == 2:
        print('28')
    else:
        print('30')