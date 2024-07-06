a=int(input("enter cost of bike"))
c=0
if a>100000:
    c=15/100*a
    print("tax valu is 15%",c)
elif a>50000 and a<=100000:
    c=10/100*a
    print("tax valu is 10%",c)
elif a<=50000:
    c=5/100*a
    print("tax valu is 5%",c)
else:
    print("no tax")