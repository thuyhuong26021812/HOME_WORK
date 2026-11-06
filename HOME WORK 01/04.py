#: Viết chương trình nhập vào một “kí tự”, Kiểm tra xem c có phải là kí tự chữ cái không (hoa hoặc thường). Nếu đúng thì in ra “{c} là kí tu alphabet”, nếu sai in ra “{c} không phải là kí tự alphabet. 

def main(n):
    if ('a' <= n <= 'z') or ('A' <= n <= 'Z'):
        print('{0} là kí tự alphabet'.format(n))
    else:
        print('{0} không là kí tự alphabet'.format(n))
main('6')