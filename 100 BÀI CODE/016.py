'''Viết chương trình nhập vào điểm trung bình học kỳ I và trung bình học kỳ II, tính trung
bình cả năm theo công thức:  TBCN=(TBHKI+TBHKII*2)/3. Xếp lọai theo cách:
“Gioi” nếu TBCN>=8
“Kha” nếu 6.5<=TBCN <8
“Trung binh” nếu 5.0<=TBCN <6.5
“Yeu” nếu 3.5<=TBCN <5
“Kem” nếu TBCN<3.5'''

tbhkI, tbhkII = map(float, input().split())
tbcn = (tbhkI +tbhkII*2)/3
if tbcn >= 8:
    print(f'{tbcn:.1f}','\nGioi')
elif tbcn >= 6.5:
    print(f'{tbcn:.1f}','\nKha')
elif tbcn >= 5.0:
    print(f'{tbcn:.1f}','\nTrung binh')
elif tbcn >= 3.5:
    print(f'{tbcn:.1f}','\nYeu')
else:
    print(f'{tbcn:.1f}','\nKem')