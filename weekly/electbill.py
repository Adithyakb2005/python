a=int(input("enter the unit:"))

if a<=100:
    p=0
    print("no price")
elif a<=200:
       p=(a-100)*5
       print(p)
elif a>200:
    p=(500)+(a-200)*10
    print(p)
else:
    print("invalid")