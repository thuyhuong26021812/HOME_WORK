#Viết chương trình nhập vào số học sinh của 1 lớp (HS) và số táo trong rổ (T). Hãy chia đều số táo cho tất cả học sinh trong lớp, mỗi bạn sẽ được bao nhiêu quả táo? Còn dư lại bao nhieu quả?

t , hs = map(int, input().split())
t_hs = t//hs
t_du = t%hs
print(t_hs, t_du)

