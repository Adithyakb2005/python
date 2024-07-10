#LAMBDA***

# add=lambda a,b:a+b
# print(add(10,10))



# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# div=lambda a,b:a/b
# mul=lambda a,b:a*b

# def number():
#     a=int(input("enter first no:"))
#     b=int(input("enter second no:"))
#     return a,b
# while True:
#     print("\n 1.add \n 2.sub \n 3.div \n 4.mul \n 5.exit")
#     ch=int(input("enter the choice:"))
#     if ch==1:
#         a,b=number()
#         print(add(a,b))
#     elif ch==2:
#         a,b=number()
#         print(sub(a,b))
#     elif ch==3:
#         a,b=number()
#         print(div(a,b))
#     elif ch==4:
#         a,b=number()
#         print(mul(a,b))
#     elif ch==5:
#         break

#         a,b=number()
#         print(div(a,b))
#     elif ch==4:
#         a,b=number()
#         print(mul(a,b))
#     elif ch==5:
#         break


#MAP METHOD***

# l=[1,2,3,4,5]
# data=list(map(lambda a:a**2,l))
# """print(data)
# print(list(data))"""

# def fun1(a):
#     return a**2
# data1=map(fun1,l)
# print(list(data1))

#FILTER

# data=filter(lambda a:a%2==0,l)
# print(list(data))

# def fun1(a):
#     return a%2==0
# data1=filter(fun1,l)
# print(list(data1))

#string

# l=['apple','mango']
# data=filter(lambda a:a[0]=='a',l)
# print(list(data))

# def fun1(a):
#     return a[0]=='a'
# data1=filter(fun1,l)
# print(list(data1))


#REDUCE

import functools
l=[1,2,3,4,5]
data=functools.reduce(lambda total,value:total+value,l)
print(data)

def fun1(totel,value):
    return totel+value
data=functools.reduce(fun1,l)
print(data)