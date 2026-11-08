# Bài 8
a, b, c, d, m, n = map(float, input().split())
if a*d - c*b != 0:
    x = (b*n - m*d)/(b*c - a*d)
    y = (m*c - a*n)/(b*c - a*d)
    print(f'Phuong trinh tuyen tinh: {a}x + {b}y = {m} và {c}x + {d}y = {n}', f'\nNghiem của he phuong trinh: (x,y) = ({x},{y})')
elif a*d - c*b == 0:
    print('Phuong trinh vo nghiem')