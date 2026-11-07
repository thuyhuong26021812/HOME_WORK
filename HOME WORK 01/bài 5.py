# Bài 5: Nhập vào chữ cái hoa A, in ra chữ cái thường liền trước chữ cái a thường tương ứng của A. Xét TH khi c = ‘A’ là đặc biệt.
c = input('Nhập kí tự: ')
if (c == 'A'):
    print('A')
elif (c != 'A') and (chr(ord(c) - 1).isupper()):
    print(chr(ord(c) - 1).lower())