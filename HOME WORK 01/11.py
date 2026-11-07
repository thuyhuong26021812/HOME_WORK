# 11. Kiểm tra năm sinh và tính tuổi: Nhập năm sinh, tính tuổi hiện tại (giả sử năm hiện tại là 2025), và kiểm tra xem người đó có đủ 18 tuổi hay chưa.

n = int(input('Năm sinh: '))
tuoi = 2025 - n
if tuoi < 18:
    print('Chưa đủ 18')
else:
    print('Đã đủ 18')