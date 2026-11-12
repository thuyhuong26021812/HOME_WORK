# Viết chương trình nhập vào 3 số nguyên a, b, c; in ra số lớn nhất, nếu 3 số bằng nhau thì in dấu "="

a, b, c = map(int, input().split())
if a == b ==c:
    print('=')
else:
    print(max(a,b,c))