# hàm nhận đầu vào n và in ra số thứ n trong dãy fibonaci
def fibonaci_n(n:int)->int:
    if n==0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    for i in range(2,n+1):
        a,b=b,a+b
    return b

assert fibonaci_n(2)==1
assert fibonaci_n(3)==2
assert fibonaci_n(4)==3
assert fibonaci_n(5)==5
print('Accepted')

# hàm tìm giá trị lớn nhất trong dãy
def solonnhat(day_so):
    """
tìm ra số lớn nhất trong dãy nhập vào
parameter:day_so(list) dãy số cần xét chứa số nguyên hoặc số thực
assumptions:day_so không được rỗng,phải có ít nhất một phần tử
returns:int hoặc float -giá trị lớn nhất tìm được
    """
    solonnhat=day_so[0] 
    for so in day_so:
        if so>solonnhat:
            solonnhat=so
    return solonnhat
assert solonnhat([1,2,3,4,5,6])==6 ,'sai với danh sách số dương'#nếu mình kiểm tra sai nó sẽ hiện chữ này
assert solonnhat([-1,-4,-3])==-1,'sai với danh sách số âm'
print('Accepted')

# hàm kiểm tra xem có phải số nguyên tố không
def snt(n:int):
    '''
    kiểm ta xem số n nhập vào có phải số nguyên tố hay không
    parameter:
    n:số tự nhiên (int)
    assumption:
    n:số nguyên(n>=0)
    return:
    True nếu nó là số nguyên tố
    False nếu nó không phải số nguyên tố
    '''
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
             return False
    return True
assert snt(3)==True,'3 là số nguyên tố'
assert snt(4)==False,'4 không phải số nguyên tố'
assert snt(5)==True,'5 là số nguyên tố'
print('Accepted')

# hàm kiểm tra năm nhuận
def namnhuan(n:int):
    '''
    kiểm tra xem năm nhập vào có phải năm nhuận hay không
    parameter:
    n:số năm nhập vào(int)
    assumption:
    n:số nguyên (n>=0)
    returns:
    True nếu năm n là năm nhuận
    False nếu năm n không phải năm nhuận
    '''
    if n%400==0 or (n%4==0 and n%100!=0):
        return True
    else:
        return False
assert namnhuan(2000)==True,'năm 2000 là năm nhuận'
assert namnhuan(2024)==True,'năm 2024 là năm nhuận'
assert namnhuan(2018)==False,'năm 2018 không phải năm nhuận'
print('Accepted')

# tính số tiền điện
def dongia(sodien,heso=3000):
    '''
    tính đơn giá điện
    parameter:
    sodien:số điện nhập vào(float)
    assumption:
    sodien:là số nguyên ,sodien>0
    return:
    đơn giá điện gồm số điện và số tiền điện đi kèm
    '''
    sotien=sodien*heso
    return sotien
assert dongia(100)==300000
assert dongia(200)==600000
print('Accepted')

# viết hàm nhập vào hai số a,b trả về số lớn hơn trong hai số
def solonhon(a,b:int)->int:
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return 'hai số bằng nhau'
assert solonhon(2,3)==3
assert solonhon(2,2)=='hai số bằng nhau'
assert solonhon(5,3)==5,'số 5 lớn hơn số 3'
print('Accepted')

# viết hàm hoán đổi hai số nguyên
def haisonguyen(a,b):
    return (b,a)
assert haisonguyen(2,3)==(3,2)
assert haisonguyen(3,4)==(4,3)
print('Accepted')

# viết hàm kiểm tr một số có phải số nguyên tố không
def snt(n:int):
    '''
    kiểm tra xem một số có phải số nguyên tố hay không
    parameter:
    n:số cần xét(int)
    assumption:
    n:là số nguyên ,n>=0
    return:
    True nếu là số nguyên tố
    False nếu không phải số nguyên tố
    '''
    if n==0:
     return False
    if n==1:
     return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
assert snt(9)==False,'số 9 không phải số nguyên tố'
assert snt(7)==True
assert snt(1)==False
print('Accepted')

# viết hàm kiểm tra một số có phải số hoàn hảo không
def shh(n:int):
    '''
    kiểm tra một số có phải số hoàn hảo không
    parameter:
    n:số cần kiểm tra(int)
    assuption:
    n:số nguyên,n>0
    return:
    True nếu là số hoàn hảo
    False nếu không phải số hoàn hảo
    '''
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
    if tong==n:
     return True
    else:
     return False
assert shh(6)==True
assert shh(8)==False
assert shh(28)==True
print('Accepted')

# viết hàm đưa vào một list  số nguyên và một số nguyên dương k ,viết hàm trả về vị trí của phần tử đầu tiên có giá trị k trong dãy không có thì trả về 1
def vitri(day_so:list,k:int)->int:
   '''
   trả về vị trí của số có giá trị bằng k trong dãy
   parameter:
   day_so:dãy số cần xét(list)
   k:số cần xét(int)
   assumption:
   day_so:có ít nhất một phần tử
   k:là số nguyên,k>0
   return:
   vị trí của số có giá trị bằng k trong dãy
   '''
   if k in day_so:
       return day_so.index(k)
   else:
       return -1
assert vitri([1,2,3,4,5],3)==2
assert vitri([1,2,3,4,5,6],7)==-1
print('Accepted') 