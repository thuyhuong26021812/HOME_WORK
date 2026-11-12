# Nhập vào số xe (có năm chữ số) trong biển số xe máy của bạn. Cho biết số xe của bạn được mấy nút. Bạn là người may mắn nếu số nút=9. Bạn có may mắn không?

n = input()
tong = 0
for i in n:
    tong += int(i)
    mod = tong % 10 
if mod == 9:
    print( mod, '\nmay man')
else:
    print(mod, '\nchua may man')