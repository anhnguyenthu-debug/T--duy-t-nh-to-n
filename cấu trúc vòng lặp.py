for i in range(10):
 print(f'{i+1}.hello world')
#   cho một list 2 chiều# đưa về list một chiều
 lst=[[1,2,3],[2,3,5,6,7],[2,3,7,8,9]]
lst_output=[]
for i in range(len(lst)):
  for j in range(len(lst[i])):
     lst_output.append() 
print(lst[:1])
#   trong danh sách có số chẵn không
lst=[1,2,3,5,8,9,13,133,14]
check=False
for x in lst:
  if x%2==0:
    check=True
    break
if check:
  print('yes')
else:
  print('no')
print('no') 
# nhập vào một số nguyên đến khi được 1 số nguyên dương