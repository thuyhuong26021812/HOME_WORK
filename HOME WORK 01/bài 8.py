# Bài 8:
import textwrap
ten = input('Ten chu ho: ')
so_cu = int(input('Chi so thang truoc: '))
so_moi = int(input('Chi so thang nay: '))
so_kwh = so_moi - so_cu
tien = 0
if so_kwh <= 50:
    tien = so_kwh * 1984
elif 50 < so_kwh <= 100:
    tien = 50 * 1984 + (so_kwh - 50)* 2050
elif 100 < so_kwh <= 200:
    tien = 50 * 1984 + 100*2050 + (so_kwh - 100)* 2380
elif 200 < so_kwh <= 300:
    tien = 50 * 1984 + 100*2050 + 100*2380+ (so_kwh - 100)* 2998
elif 300 < so_kwh <= 400:
     tien = 50 * 1984 + 100*2050 + 100*2380 + 100*2998 + (so_kwh - 100)* 3350
elif so_kwh > 400:
     tien = 50 * 1984 + 100*2050 + 100*2380 + 100*2998 + 100* 3350 + (so_kwh - 100)* 3460
print(f'Ho va ten: {ten}\nTien phai tra la: {tien}')
