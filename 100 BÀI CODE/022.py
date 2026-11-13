# Viết chương trình nhập vào số KW/h điện tiêu thụ trong 1 tháng và tính tiền điện sử dụng trong 1 tháng đó. Biết rằng, 50 KW/h đầu được tính với giá 600đ mỗi KW/h, 50KW/h tiếp theo được tính với giá 800đ mỗi KW/h, 100 KW/h tiếp theo được tính với giá 1100đ mỗi KW/h, những KW/h tiếp theo được tính với giá 1500đ mỗi KW/h.

n = int(input())
if n>200:
    print(50*600 + 50*800 + 100*1100 + (n-200)*1500)
elif n>100:
    print(50*600 + 50*800 + (n-100)*1100)
elif n>50:
    print(50*600 + (n-50)*800)
else:
    print(n*600)