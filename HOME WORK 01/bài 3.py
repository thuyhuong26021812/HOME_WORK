# Bài 3: Viết chương trình nhập vào một “kí tự” c, nếu nó là chữ hoa thì in ra chữ thường tương ứng và ngược lại nếu nó là chữ thường thì in ra chữ hoa tương ứng của nó. (xem trước cấu trúc lựa chọn: if….else, ma) 
c = input('Nhập kí tự: ')
if c.isupper():
    print(c.lower())
elif c.islower():
    print(c.upper())
