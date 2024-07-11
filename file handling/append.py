# f=open("python/file handling/appnew.txt","a")
# f.write(" hello")

# f=open("python/file handling/appnew.txt","r")
# print(f.read())
# print(f.read(14))
# print('-'*20)
# print(f.read(6))
# print(f.readline(9))
# print('-'*20)
# print(f.readline(5))
# print(len(f.readline()))
f=open("python/file handling/appnew.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
letter=0
c=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j ==' ':
            word+=1
        else:
            letter+=1
            if j.isupper():
                c+=1
    # print(a[::-1])
    word+=1
print("words:",word)
print("letter:",letter)
print("capital letter:",c)
print("small letter:",letter-c)