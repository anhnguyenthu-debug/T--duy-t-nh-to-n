# nhập vào một tháng và năm dưới dạng số nguyên kiểm tra xem tháng đó có bao nhiêu ngày
maxday='error'
thang,nam=map(int,input().split('/'))
match thang:
    case 1|3|5|7|8|10|12:
        maxday=31
    case 4|6|9|11:
        maxday=30
    case 2:
        if((nam%4==0 and nam%100) or (nam%400==0)):
            maxday=29
        else:
            maxday=28
    
print(maxday)
