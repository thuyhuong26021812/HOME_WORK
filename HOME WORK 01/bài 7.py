# Bài 7: Nhập vào một chuỗi gồm các kí tự thường độ dài >=20, in ra chữ cái thứ năm và thứ chín của chuỗi này
import textwrap
s = str(input('Nhap chuoi: '))
if len(s) < 20:
    print('Chuoi khong hop le')
else:
    print('Ki tu thu nam la: ', s[4],'\nKi tu thu chin la:',s[8] )