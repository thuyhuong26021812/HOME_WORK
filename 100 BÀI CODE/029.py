'''Viết chương trình nhập vào 1 số nguyên dương n. Cho biết n có phải là số nguyên tố
hay không? Số nguyên tố là số chỉ chia hết cho 1 và chính nó (chỉ có 2 ước)
Vd: n=7 là số nguyên tố vì 7 chỉ chia hết cho 1 và 7
n=8 Không là số nguyên tố vì 8 chia hết cho 1 và 8 nhưng còn chia hết cho 2 và 4'''

n = int(input())
m = []
for i in range(1,n+1):
    if n % i == 0:
        m.append(i)
if len(m) > 2:
    print('No')
elif len(m) == 2:
    print('Yes') 