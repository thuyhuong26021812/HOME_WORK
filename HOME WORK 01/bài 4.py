# Bài 4. Viết chương trình nhập vào một “kí tự”, Kiểm tra xem c có phải là kí tự chữ cái không (hoa hoặc thường). Nếu đúng thì in ra “{c} là kí tu alphabet”, nếu sai in ra “{c} không phải là kí tự alphabet

c = input('Nhập vào kí tự: ') 
if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
    print('{0} là kí tự alphabet'.format(c))
else:
    print('{0} không là kí tự alphabet'.format(c))
