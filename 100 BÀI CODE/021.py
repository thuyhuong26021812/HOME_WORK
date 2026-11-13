n = int(input())
if n>30:
    print(12000 + 29*10000 + (n-30)*9000)
elif n>=2:
    print(12000 + (n-1)*10000)
elif n==1:
    print(12000)
