m, n = map(int, input().split())
a = []
for i in range(m, n+1):
    b = []
    for j in range(1, n+1):
        k= i%j
        if k==0:
            b.append(j)
    if len(b)==2:
        a.append(i)
print(len(a))
