# nhập vào 4 số tìm số có giá trị lớn thứ 2
a,b,c,d=map(float,input().split())
if a>b or a>c or a>d and a>c or a>b or a>d  and a<d or a<b or a<c:
    print('số lớn thứ hai {}'.format(a))
elif b>a or b>c or b>d and b>c or b>d or b>a and b<d or b<a or b<c:
    print('số lớn thứ hai {}'.format(b))
elif c>a or c>b or c>d and c>b or c>d or c>a and c<d or c<a or c<b:
    print('số lớn thứ hai {}'.format(c))
elif d>a or d>b or d>c and d>b or d>a or d>c and d<c or d<b or d<a:
    print('số lớn thứ hai {}'.format(d))