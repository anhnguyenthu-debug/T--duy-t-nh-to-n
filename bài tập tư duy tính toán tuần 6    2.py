# nhập vào số nguyên n và trả về giai thừa của n
# def giaithua(n:int)->int:
#     '''
#     nhập vào số n và trả về giai thừa của n
#     parameter:
#     n:là số cần tính giai thừa
#     assumption:
#     n:số nguyên dương
#     return:
#     giai thừa của n
#     '''
#     tich=1
#     for i in range(1,n+1):
#         tich*=i
#     return tich
# assert giaithua(2)==2
# assert giaithua(5)==120
# assert giaithua(6)==720
# print('Accepted')

# viết hàm giả lập máy tính bỏ túi
# def maytinh(a:float,dau:str,b:float):
#     '''
#     nhập vào hai số a,b và dấu phép tính +-*: trả về kết quả cộng trừ nhân chia tương ứng
#     parameter:
#     một phép tính đầy đủ cần tính
#     assumption:
#     a,b là số thực,nếu là phép chia b!=0
#     dấu là một trong 4 dấu +-*:
#     return:
#     kết quả phép tính
#     '''
    
#     if dau=='+':
#         ketqua=a+b
#     elif dau=='-':
#         ketqua=a-b
#     elif dau=='*':
#         ketqua=a*b
#     elif dau==':':
#         ketqua=a/b if b!=0 else 'Error'

#     return round(ketqua,2)
# assert maytinh(5,'+',4)==9
# assert maytinh(5,':',4)==1.25
# assert maytinh(5,'*',4)==20
# assert maytinh(5,'-',4)==1
# print('Accepted')

# viết hàm trả về tổng của các chữ số của số nguyên dương n
# def tongchuso(n:int):
#     '''
#  nhập vào số nguyên dương n,trả về tổng các chữ số của nó
#  parameter: n là số cần tính tổng các chữ số
#  assumption:n là số nguyên dương(int)
#  return:tổng của các chữ số của n
#     '''
#     tong=0
#     while n>0:
#      n%10
#      tong+=n%10
#      n=n//10
#     return tong
# assert tongchuso(10)==1
# assert tongchuso(123)==6
# assert tongchuso(505)==10
# print('Accepted')

# nhập vào hai số nguyên x,y trả về khoảng cách hamming giữa hai số này
def hamming(x,y):
    ''' 
    nhập vào hai số nguyên x,y trả về khoảng cách hamming giữa hai số này
    parameter:x,y là hai số cần so sánh
    assumption:x,y là hai số nguyên(float)
    return:khoảng cách hammming giữa hai số
    '''
    nhiphanx=bin(x)[2:]
    nhiphany=bin(y)[2:]
    dodai=max(len(nhiphanx),len(nhiphany))
    nhiphanx=nhiphanx.zfill(dodai)
    nhiphany=nhiphany.zfill(dodai)
    tong=0
    for i in range(1,dodai):
        if nhiphanx[i]!=nhiphany[i]:
            tong+=1
    return tong
assert hamming(2,3)==1
assert hamming(3,4)==2
print('Accepted')

# viết hàm kiểm tra một tích có chia hết cho 10 không
def is_product_divisible_by_10(a,b):
    '''
    kiểm tra tích a và b có chia hết cho 10 không
    parameter:a,b là hai thừa số của tích
    assumption:a,b là số thực (float)
    return :True nếu chia hết và False nếu không chia hết
    '''
    c=a*b
    return True if c%10==0 else False
assert is_product_divisible_by_10(2,3)==False
assert  is_product_divisible_by_10(6,5)==True
assert is_product_divisible_by_10(0,1)==True
print('Accepted')

# viết hàm nhập vào hai số và trả về thương và số dư 
def devide_with_reminder(a,b):
    '''
    nhập vào hai số trả về thương và dư
    parameter:a,b là số bị chia và số chia
    assumption:số b phải khác 0,a,b là số thực
    return thương và số dư
    '''
    if b!=0:
     q=a//b
     r=a%b
    else:
      return 'Error'
    return (q,r)

assert devide_with_reminder(10,3)==(3,1)
assert  devide_with_reminder(5,5)==(1,0) 
print('Accepted')          

# viết hàm nhập vào 3 số a,b,c kiểm tra xem ba số có phải cạnh một tam giác không
def is_right_triangle(a,b,c):
   '''
   nhập vào ba số a,b,c kiểm tra xem ba số có phải độ dài ba cạnh tamm giác không
   parameter:ba số đo đọ dài của ba cạnh
   asumption:a,b,c là số tự nhiên(int)
   return True nếu là độ dài 3 cạnh tam giac,False nếu không phải
   '''
   if a+b>c and a+c>b and b+c>a:
      return True
   else:
      return False
assert is_right_triangle(3,4,5)==True
assert is_right_triangle(3,4,4)==True
assert is_right_triangle(3,1,2)==False
print('Accepted')



  