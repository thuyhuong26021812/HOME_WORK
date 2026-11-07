# 2.Kiểm tra số có tận cùng 5 không: Viết chương trình nhập một số nguyên, kiểm tra số đó có tận cùng 5 không, nếu đúng in ra “True”, nếu sai in ra “False”. 

n = float(input())
if n%5 == 0 and n%2 == 1:
    print('True')
else:
    print('False')