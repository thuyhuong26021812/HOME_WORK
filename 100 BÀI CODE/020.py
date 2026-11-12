# Nhập một số tiền N (N<=1.000.000) đồng (N là số chia hêt cho 1.000), đổi ra xem được bao nhiêu tờ 5.000 đồng, bao nhiêu tờ 2.000 đồng, bao nhiêu tờ 1.000 đồng sao cho tổng số tờ là ít nhất. Ví dụ N= 43.000 đ = 8 tờ 5.000 đ + 1 tờ 2.000 đ + 1 tờ 1.000 đ.

n = int(input())
print(n//5000, n%5000//2000, f'{n%5000%2000/1000:.0f}')