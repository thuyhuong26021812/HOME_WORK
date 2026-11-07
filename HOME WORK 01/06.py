# 6. Kiểm tra ký tự nhập vào là chữ hay số: Viết chương trình nhập một ký tự, kiểm tra xem ký tự đó là chữ cái hay số. 
ki_tu = input()
if 'a' <= ki_tu <= 'z' or 'A' <= ki_tu <= 'Z':
    print(f'{ki_tu} là chữ cái')
else:
    print(f'{ki_tu} là chữ số')

# cách khác:
if ki_tu.isalpha():
    print(f'{ki_tu} là chữ cái')
elif ki_tu.isdigit():
    print(f'{ki_tu} là chữ số')