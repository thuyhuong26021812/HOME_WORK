# 4.Kiểm tra tuổi đủ điều kiện bầu cử: Viết chương trình nhập năm sinh của một người, kiểm tra xem người đó có đủ 18 tuổi để đi bầu cử hay không
n = int(input('Nhập số tuổi hiện tại: '))
if n < 18:
    print('Không đủ điều kiện bầu cử')
else:
    print('Đủ điều kiện bầu cử')