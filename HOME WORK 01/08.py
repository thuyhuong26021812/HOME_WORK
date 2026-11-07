# 8. Kiểm tra năm nhuận: Viết chương trình nhập năm, kiểm tra xem năm đó có phải năm nhuận hay không. (Năm nhuận nếu chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100) 

n = int(input('Nhập số năm: '))
if n%400 == 0 or ( n%4 == 0 and n%100 != 0):
    print(f'{n} là năm nhuận')
else:
    print(f'{n} không là năm nhuận')