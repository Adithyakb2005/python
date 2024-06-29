l=[1,2,3,'abc',20.5]
sum=0
for i in l:
    if type(i)==int or type(i)==float:
        sum=sum+i
print(sum)