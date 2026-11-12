# Viết chương trình tính chu vi và diện tích hình chữ nhật, với chiều dài a và chiều rộng b là các số tự nhiên theo công thức cv=(a+b)*2, dt=a*b.

a, b = map(int, input().split())
cv = 2*(a+b)
dt = a*b
print(cv, dt)