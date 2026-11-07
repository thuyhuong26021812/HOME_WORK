c = input('Nhập kí tự: ')
if (c == 'A'):
    print('A')
elif (c != 'A') and (chr(ord(c) - 1).isupper()):
    print(chr(ord(c) - 1).lower())