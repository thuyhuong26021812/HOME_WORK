# Hai số nguyên dương m và n trên cùng 1 dòng, cách nhau bởi dấu cách

m, n = map(int, input().split())
for i in range(m, n+1):
    a = []
    for j in range(1, n+1):
        if i%j==0:
            a.append(j)
    if len(a)==2:
        print(i, end=' ')
if len(a)>2:
    print('-')