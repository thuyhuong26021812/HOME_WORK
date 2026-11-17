k = int(input())
a = []
i = 2
while len(a) < k:
    b = []
    for j in range(1, i+1):
        if i % j == 0:
            b.append(j)
    if len(b) == 2:
        a.append(i)
    i += 1
print(*a, end=' ') 