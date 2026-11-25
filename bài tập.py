a,b,c=map(float,input().split())
if a>b and a<c :
    print('số lớn thứ hai là {}'.format(a))
elif b>c and b<a :
    print('số lớn thứ hai là {}'.format(b))
elif c>b and c<a :
    print('số lớn thứ hai là {}'.format(c))