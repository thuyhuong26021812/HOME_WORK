# Bài 1: Nhập vào 2 cạnh của một hình chữ nhật. In ra màn hình diện tích và chu vi của nó.  

a, b = map(float, input(f'Chiều dài và chiều rộng: ').split())
dien_tich = a*b
chu_vi = 2*(a+b)
print(f'Diện tích hcn là: {dien_tich} \nChu vi hcn là: {chu_vi}')
