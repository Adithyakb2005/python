def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def number():
    a=int(input("enter first no:"))
    b=int(input("enter second no:"))
    return a,b
while True:
    print("\n 1.add \n 2.sub \n 3.div \n 4.mul \n 5.exit")
    ch=int(input("enter the choice:"))
    if ch==1:
        a,b=number()
        print(add(a,b))
    elif ch==2:
        a,b=number()
        print(sub(a,b))
    elif ch==3:
        a,b=number()
        print(div(a,b))
    elif ch==4:
        a,b=number()
        print(mul(a,b))
    elif ch==5:
        break