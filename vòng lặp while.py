# đếm từ 1 đến 5
# n=int(input())
# i=1
# while i<=n:
#     print(i,end=' ')
#     i+=1
  
# lập lại lời chào
# loichao=str(input())
# dem=1
# while dem<=5:
#     print(loichao)
#     dem+=1

# nhập mật khẩu
# matkhau=''
# while matkhau!='1234':
#   matkhau=input('xim mời nhập mật khẩu: ')
# print('Xin mời' )
# luyện tập giảm biến đếm:
# n=int(input())
# x=n
# while x>=0:
#     print(x)
#     x-=1
# print('Phóng tên')

# in các số chẵn từ 1 đến n
# n=int(input())
# x=1
# while x<=n:
#     if x%2==0:
#         print(x,end=' ')
#     x+=1

# luyện biến cộng dồn,tính tổng các số từ 1 đến n
# n=int(input())
# x=1
# tong=0
# while x<=n:
#     tong+=x
#     print(x,end=' + ') if x<n else print(x,end=' = ')
#     x+=1
# print(tong)

# thu tiền
# n=int(input())
# ngankho=0
# while ngankho<n:
#     nop=int(input('Mời nộp thêm: '))
#     ngankho+=nop
# print('Đã đủ')

# in ra các số vừa chia hết cho 2 vừa chia hết cho 3 trong khoảng từ 1 đến n
# n=int(input())
# x=1
# while x<=n:
#     if x%2==0 and x%3==0:
#         print(x,end=' ')
#     x+=1

# tính giai thừa từ 1 đến n
# n=int(input())
# giaithua=1
# tong=0
# x=1
# while x<=n:
#     giaithua*=x
#     print(giaithua,end=' + ') if giaithua<giaithua*n else print(giaithua,end=' = ')
#     tong+=giaithua
#     x+=1
# print(tong)
# 

# tính tổng các số nguyên từ 1 đến n
   # for
# n=int(input())
# tong=0
# for x in range(1,n+1):
#     tong+=x
# print(tong)
   #while
# n=int(input())
# x=1
# tong=0
# while x<=n:
#     tong+=x
#     x+=1
# print(tong)     

# viết trương trình nhập vào một số cho tới khi được số nguyên dương thì thôi,kiểm tra xem có phải số nguyên tố không
# n=int(input())
# while n<=0:
#     n=int(input('Mời nhập số: '))

# if n==1:
#     print('không là số nguyên tố')
# else:
#     la_so_nguyento=True
# for x in range(2,n):
#     if n%x==0:
#         la_so_nguyento=False
#         break
# if la_so_nguyento:
#     print('Là số nguyên tố')
# else:
#     print('không là số nguyên tố')

# tính giai thừa của một số nguyên cho trước
# cách 1 :For
# n=int(input())
# tich=1
# for x in range(1,n+1):
#     tich*=x
# print(tich)
# cách 2 :While
# n=int(input())
# x=1
# tich=1
# while x<=n:
#     tich*=x
#     x+=1
# print(tich)
# viết chương trình nhập vào một số nguyên và in ra số chữ số của số đó
# cách 1:While
# n=abs(int(input()))
# dem=0
# while n>0:
#     n=n//10# ý nghĩa là trong vòng lặp while này,khi nào n còn lớn hơn 0 thì ta cứ lấy phép chia lấy phần nguyên của n cho 10 cho đến khi nào được 0 thì thôi ,số lần tích như vậy chính là số chữ số của số n
#     dem+=1
# print(dem)

# nhập vào một số n và một dãy số gồm n số nguyên ,kiểm tra xem có số 42 hay không
# n=int(input())#nhập vào số phần tử của dãy
# day=list(map(int,input().split()))
# tim_thay=False#cắm cờ,hiện tại chưa xét,chưa tìm thấy 42 nên cắm cờ không tìm thấy
# x=0#tạo biến đếm
# while x<n:#khời tạo vòng lặp
#     if day[x]==42:
#         tim_thay=True
#         break
#     x+=1
# print('ta đã tìm thấy ý nghĩa của cuộc sống') if tim_thay==True else print('Vớ vẩn')

# kiểm tra xem một dãy nhập vào có chứa số 42 không
n=int(input())
day=list(map(int,input().split()))
tim_thay=False
x=0
while x<n:
    if day[x]==42:
        tim_thay=True
        break
print('đã tìm thấy') if tim_thay else print('không tìm thấy')