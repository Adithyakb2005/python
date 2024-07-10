# a=int(input("enter the number"))
# f=open('python/file handling/multiple','w')
# for i in range(1,11):
#     f.write(f"{a} x {i} = {a*i}\n")

a=int(input("enter the number"))
f=open('python/file handling/multiple1','w')
for i in range(1,a+1):
    f.write(f"multiplication table {i}:\n")
    for j in range(1,11):
        f.write(f"{j} x {i} = {a*j}\n")
    f.write("\n")
f.close()