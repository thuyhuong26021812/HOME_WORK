# Viết chương trình nhập vào điểm Toán, Văn, Anh văn của 1 học sinh là các số thực. Tính trung bình của học sinh đó, biết rằng điểm Toán, Văn là hệ số 2

toan, van, anhvan = map(float, input().split())
trung_binh = ((toan + van)*2 + anhvan)/5
print(f'{trung_binh:.1f}')