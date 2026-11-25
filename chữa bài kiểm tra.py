# viết chương trình cho đầu vào là ngày tháng năm dưới dạng dd/mm/yyyy cho đầu ra là ngày liền tiếp sau đó đưới dạng dd/mm/yyyy
# 
# đồng hồ điện tử sau 1 s
# h,m,s=map(int,input().split(':'))
# max_s=59
# max_m=59
# max_h=23
# if s==max_s:
#     if m<max_m:
#         s=0
#         m+=1
#         h=h
#     elif m==max_m:
#         s=0
#         m=0
#         h=h+1 if h<max_h else 0
# else:
#     s+=1
#     m=m
#     h=h
# print(f'{h:02d}:{m:02d}:{s:02d}')


# đồng hồ đếm ngược
h,m,s=map(int,input().split(':'))
min_h=0
min_m=0
min_s=0
if s==min_s:
    if m==min_m:
        h=h-1 if h>min_h else 23
        m=59
        s=59
    else:
        s=59
        m=m-1
else:
    s=s-1
print(f'{h:02d}:{m:02d}:{s:02d}')


