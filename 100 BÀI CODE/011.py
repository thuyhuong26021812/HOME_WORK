# Viết chương trình nhập vào tổng số giây là một số nguyên, in ra giờ:phút:giây

s = int(input())
h = s//3600
m = (s%3600)//60
seconds = s - h*3600 - m *60
print(h,m,seconds, sep = ':')