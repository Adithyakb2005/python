# a=20
# def fun():
#     a=10
#     a=a+10
#     print('welcome',a)
# fun()
# print('outsidefun',a)


# def fun1():
#     global b 
#     b=10
#     print("welcome",b)
#     c=10
#     return c,43

# #print(fun1())
# c1,d1=fun1()
# # c1=fun1()
# print("outside",c1,d1)


#TYPE OF ARRGUMENTS

#position arr

# def add(a,b):
#     return a+b
# print(add(10,20))
# print(add(10,30))
# print(add('asd','as123'))

#fun with default para value

# def add(name,age=24):
#     return name,age
# print(add('anu',25))
# print(add('sanu'))

#fun with keyword arrgument

# def add(name,age):
#     print("name:",name)
#     print("age",age)
# add('anu',25)
# add(age=24,name='sanu')

#arbitery arrgument

# def add(*a):
#     return a
# print(add('anu',25))
# print(add())

#arbetery keyword

def add(**a):
     return a
print(add(name='anu',age=25))
print(add())
