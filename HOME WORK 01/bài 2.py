# Bài 2: Một khu đất hình chữ nhật có chiều rộng a, chiều dài b. Người ra xây một khu vui chơi hình tròn tại vị trí trung tâm khu đất như hình vẽ. Nhập vào a, b. Hãy tính phần diện tích còn để trồng cây xung quanh là bao nhiêu. Biết pi = 3.14, lấy kết quả đến 2 chữ số phần thập phân.
import math
a, b = map(int, input('nhập độ lớn cạnh: ').split())
dien_tich_hcn = a*b
dien_tich_hinh_tron = math.pi*((b/2)**2)
dien_tich_con_lai = dien_tich_hcn - dien_tich_hinh_tron
print(f'Diện tích trồng hoa là: {dien_tich_con_lai:.2f}')
    
