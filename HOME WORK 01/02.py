import math
def length_width(a,b):
    dien_tich_hcn = a*b
    dien_tich_hinh_tron = math.pi*((b/2)**2)
    dien_tich_con_lai = dien_tich_hcn - dien_tich_hinh_tron
    return dien_tich_con_lai
print(f'Diện tích trồng hoa là: {length_width(3,2):.2f}')
    
