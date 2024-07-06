std=[]
while True:
    print("\n 1.Add,\n 2.view,\n 3.update,\n 4.delete,\n 5.exit")
    ch=int(input("enter or choice:"))
    if ch==1:
        name=input("enter the name:")
        age=int(input("enter age:"))
        cls=input("enter or class:")
        std.append([name,age,cls])
    elif ch==2:
        for i in std:
            print(i)
    elif ch==3:
        f=0
        a=input("enter name:")
        for i in std:
            if a in i:
                name=input("enter new name:")
                age=int(input("enter new age:"))
                cls=input("enter new class:")
                i[1]=age
                f=1
            if f==0:
                print("std not available")
    elif ch==4:
        d=input("enter the name:")
        for i in std:
            if d in i:
                std.remove(d)
            else:
                print("not avilable")
