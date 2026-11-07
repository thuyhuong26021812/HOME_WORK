# 3.Kiểm tra số có chia hết cho 3 và 5 không: Viết chương trình nhập một số nguyên, kiểm tra số đó có chia hết cho 3 và 5 không, nếu đúng in ra “True”, nếu sai in ra “False”

n = int(input())
if n%3 == 0 and n%5 == 0:
    print('True')
else: 
    print('False')