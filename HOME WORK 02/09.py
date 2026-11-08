# Bài 9: Nhập vào thời gian 1 công việc nào đó là x giây. Hãy chuyển đổi và viết ra màn hình số thời gian trên dưới dạng bằng bao nhiêu giờ, bao nhiêu phút, bao nhiêu giây. 
seconds = float(input('thoi gian 1 cong viec la (giay): '))
h = seconds//3600
m = (seconds % 3600) // 60
s = seconds - h*3600 - m*60
print(f'Thoi gian 1 cong viec: {h} gio {m} phut {s} giay')
