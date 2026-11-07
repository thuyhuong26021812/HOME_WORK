import math
a, b = map(int, input('nhập độ lớn cạnh: ').split())
dien_tich_hcn = a*b
dien_tich_hinh_tron = math.pi*((b/2)**2)
dien_tich_con_lai = dien_tich_hcn - dien_tich_hinh_tron
print(f'Diện tích trồng hoa là: {dien_tich_con_lai:.2f}')
    
