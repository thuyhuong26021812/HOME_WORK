# Nhập một tháng (tây), cho biết tháng đó thuộc mùa nào (Xuân, Hạ, Thu, Ðông), biết rằng tháng 2, 3, 4 là mùa Xuân, tháng 5, 6, 7: mùa Hạ, tháng 8, 9, 10: mùa Thu, và tháng 11, 12, 1: mùa Ðông.

n = int(input())
if n in (2,3,4):
    print('Mua Xuan')
elif n in (5,6,7):
    print('Mua Ha')
elif n in (8,9,10):
    print('Mua Thu')
elif n in (11,12,1):
    print('Mua Dong')
