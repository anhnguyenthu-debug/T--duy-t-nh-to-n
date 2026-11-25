# dãy fibonanci
# n=int(input())
# sothunhat=1
# sothuhai=1
# print(sothunhat,sothuhai,end=' ')
# for x in range(1,n+1):
#  sothuba=sothunhat+sothuhai
#  sothunhat=sothuhai
#  sothuhai=sothuba
#  print(sothuba,end=' ')

# tìm số 42 trong một dãy
# n=int(input())
# day=list(map(int,input().split()))
# tim_thay=False
# x=0
# while x<n:
#     if day[x]==42:
#         tim_thay=True
#         break
#     x+=1
# if tim_thay==True:
#     print('đã tìm thấy')
# else:
#     print('không tìm thấy')

# tính tổng các số nguyên tố trong đoàn từ a đến b
# a,b=map(int,input().split())
# tong=0
# for c in range(a,b+1):
#     if c>=2:
#      snt=True
#      for x in range(2,c):
#         if c%x==0:
#            snt=False
#            break
#      if snt:
#         tong+=c
# print(tong)
# nhập vào số nguyên n vầ in ra ước nguyên tố lớn nhất của n
# n=int(input())
# max_uoc=0
# #kiểm tra xem số nào là ước của n 
# for x in range(1,n+1):
#     if n%x==0:#nếu x là ước của n
# #xét xem x có phải số nguyên tố không
#      snt=True#cắm cờ,giả sử x luôn là số nguyên tố
#      for c in range(2,x):#kiểm tra xem x có ước nào ngoài 1 và chính nó không
#         if x%c==0:#nếu có
#            snt=False#lật cờ
#            break#bỏ qua số này ,xét số tiếp theo 
#      if snt==True:
#         max_uoc=x
# print(max_uoc)


# nhập vào một số nguyên dương n,in ra các số chính phương bé hơn hoặc bằng n cùng hàng,từ bé đến lớn,có các chữ số dôi một khác nhau
# n=int(input())
# import math
# m=round(math.sqrt(n))
# for x in range(1,m+1):
#     if len(str(x*x))==len(set(str(x*x))):
#         print(x*x,end=' ')

# nhập vào một số nguyên n kiểm tr a xem số đó có bao nhiêu chữ số
# n=int(input())
# dem=1
# while dem>0:
#     n//10
#     n=n//10
#     dem+=1
#     if n//10==0:
#         break
# print(dem)

# nhập vào số n ,tìm ra và in số x trong khoảng [1,n] có độ dài dãy collatz lớn nhất
#trước đấy có một số giải thích như thế này để hình dung về cách xử lí bài toán,ta có số n là thông tin nhận được từ bên ngoài
#giả sử ta là công ty để xử lý bài toán này và đưa ra sản phẩm ,ở đây sản phẩm là số có dãy collatz dài nhất và số phép collatz thực hiện được
#trước tiên thông tin sẽ được tiếp xúc với chủ tịch,chủ địch phân tích thông tin,đưa ra mục đích và chia làm hai công việc 
#thứ nhất tìm số có dãy collatz dài nhất
#thứ hai tìm độ dài dãy đó 
#chủ tịch đưa hai công việc này cho cấp dưới
#ngay sau đó thông tin sau khi qua tay chủ tịch sẽ đến với phòng ban for
#phòng ban này sẽ xét từng số trong dãy từ 1 đến n xem số nào thỏa mãn,ở đây phòng ban sẽ phân tích thông tin và đưa ra phương án giải quyết
#đó là đếm số phép collatz được thực hiện với mỗi số ,cụ thể với mỗi x tạo ra bản sao a để phân cho nhân viên while
#mỗi nhân viên while sẽ phụ trách một số a,bắt đầu từ nhân viên while đầu tiên ,xử lí số a bằng phép collatz ,sau đó truyền cho nhân viên tiếp theo
#cứ vậy cho đến khi một nhân viên while nhận được số a=1
#lúc này sẽ tổng kết xem có bao nhiêu nhân viên while thực hiện,đó là độ dài dãy collatz ứng với số a mà nhân viên while đầu tiên tiếp nhận
#hai cái này sẽ được ghi chép và nộp lên phòng ban qua hai đầu tin a và dem
#tiếp tục như thế với các số khác trong dãy,toàn bộ thông tin sẽ được chuyển lên phòng ban,phòng ban tổng hợp và so sánh ra kết quả rồi nộp lên chủ tị
# chủ tịch sẽ tổng kết và đưa ra sản phẩm cuối ùng
#
n=int(input())#nhập vào số n
ky_luc=0#tạo biến kỷ lục bên ngoài vòng lặp
nhat=1#tại biến số ứng với kỷ lục bên ngoài vòng lặp
for x in range(1,n+1):#tạo vòng lặp xét từng số x trong khoảng từ 1 đến n
    a=x#tạo một bản sao x để thực hiện phép collatz
    dem=1
    while a!=1:#chừng nào a khác 1 thì vòng lặp vẫn tiếp diễn,vì 1 là điểm cuối của dãy collatz
        if a%2==0:
            a=a//2#nếu a chẵn thì a mới bằng một nửa a cũ
        else:#nếu a lẻ
            a=a*3+1
        dem+=1#đếm được một lần thực hiện phép collatz
    if dem>ky_luc:
        ky_luc=dem
        nhat=x
print(nhat,ky_luc)
    


