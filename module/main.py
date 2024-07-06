from reg import *
data=[]
while True:
    print("\n 1.add \n 2.display \n 3.update\n 4.delete \n 5.exit")
    ch=int(input("enter ur choice:"))
    if ch==1:
        register(data)
    elif ch==2:
        display(data)