#  7.Tính điểm học lực: Nhập điểm (0-10), phân loại học lực theo quy tắc: >=8: Giỏi; >=6.5 và <8: Khá; >=5 và <6.5: Trung bình; <5: Yếu 
n = float(input('Nhập số điểm: '))
if n < 5:
    print('Học lực yếu')
elif 5 <= n < 6.5:
    print('Học lực trung bình')
elif 6.5 <= n < 8:
    print('Học lực khá')
elif n >= 8:
    print('Học lực giỏi')