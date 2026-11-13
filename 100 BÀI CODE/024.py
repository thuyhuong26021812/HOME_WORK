n = int(input())
m = [] 
for i in range(1,n+1):
    if i % 3 == 0 :
      m.append(i)
print(len(m)) 