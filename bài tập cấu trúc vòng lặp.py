# in ra số từ 1 đến n với n được nhập từ bàn phím
# in ra các số chẵn từ 1 đến n
# n=int(input())
# for x in range(2,n+1,2):
#     print(x,end=' ')

# tính tổng s n số nguyên đầu tiên
# n=int(input())
# tong=0
# for x in range(1,n+1):
#     tong+=x
# print(tong)

# nhập vào số n và in ra bảng cửu chương của n với từ 1 đến 10
# n=int(input())
# for x in range(1,11):
#     tich=n*x
#     print('{} x {} = {}'.format(n,x,tich))

# tính giai thừ của n nhập vào từ bàn phím
# n=int(input())
# tich=1
# for x in range(1,n+1):
#     tich*=x
#     if x<n:
#         print(x,end='x')
#     else:
#         print(x,end='=')
# print(tich)

#đồng hồ đếm ngược
# h,m,s=map(int,input().split(':'))
# min_h=0
# min_m=0
# min_s=0
# if s== min_s:
#     if m==min_m:
#        m=59 
#        s=59
#        h=h-1 if h>min_h else 23
#     else:
#         s=59
#         m=m-1
# else:
#     s=s-1
# print(f'{h:02d}:{m:02d}:{s:02d}')

# nhập vào số n,tính tổng các số chia hết cho 3 hoặc cho 5 trong khoảng từ 1 đến n
# n=int(input())
# tong=0
# for x in range(1,n+1):
#     if x%3==0 or x%5==0:
#         tong+=x
# print(tong)

# đếm và liệt kê ước số
# n=int(input())
# cnt=0
# for x in range(1,n+1):
#     if n%x==0:
#         print(x,end=' ')
#         cnt+=1 
# print() 
# print(cnt)      

# tính tổng đan dấu
# n=int(input())
# tong=0
# for x in range(1,n+1): 
#  if x%2!=0:
#     tong-=x
#  else:
#     tong+=x
# print(tong)
    
# số hoàn hảo
# n=int(input())
# tong=0
# for x in range(1,1+n):
#  if n%x==0 and x<n:
#   tong+=x
# if tong==n:
#    print('{} là số hoàn hảo'.format(n))
# else:
#    print('{} không phải số hoàn hảo'.format(n))

# kiểm tra số n nhập vào từ bàn phím có phải số nguyên tố không
# n=int(input())
# cnt=0
# for x in range(1,n+1):
#     if n%x==0:
#         cnt+=1
# if cnt==2:
#             print('{} là số nguyên tố'.format(n))
# else:
#             print('{} không là số nguyên tố'.format(n))

# tổng giai thừa
# n=int(input())
# tong=0
# gt=1
# for x in range(1,n+1):
#  gt*=x
#  tong+=gt
#  if gt*x<gt*n:
#   print(gt,end='+')
#  else:
#   print(gt,end='=')
# print(tong)

# tìm ước chung lớn nhất bằng vét cạn
# a,b=map(int,input().split())
# n=min(a,b)
# for x in range(n,0,-1):
#     if a%x==0 and b%x==0:
#         break
# print(x)   

# dãy fibonacci
n=int(input())
sothunhat=1
sothuhai=2
for x in range(1,n+1):
    sothuba=sothunhat+sothuhai
    sothunhat=sothuhai
    sothuhai=sothuba
print(sothuba)

    














