"""i=1
while i<=10:
    print(i)
    i+=1"""
"""a=int(input("enter the starting no:"))
b=int(input("enter the ending no:"))
i=a
while i<=b:
    print(i)
    i+=1"""
#even
"""a=int(input("enter the starting no:"))
b=int(input("enter the ending no:"))
sum=0
i=a
while i<=b:
    if i%2==0:
        sum=sum+i
    i+=1
print(sum)"""
#odd
"""a=int(input("enter the starting no:"))
b=int(input("enter the ending no:"))
sum=0
i=a
while i<=b:
    if i%2==1:
        sum=sum+i
    i+=1
print(sum)"""
#sum
"""a=int(input("enter the starting no:"))
b=int(input("enter the ending no:"))
sum=0
i=a
while i<=b:
        sum=i+sum
        i+=1
print(sum)"""
#reverse
a=int(input("enter the number:"))
i=a
rev=0
while i>0:
    d=i%10
    i//=10
    i+=1
print(rev)