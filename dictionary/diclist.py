dtl=[{'name':'manu','age':20},{'name':'anu','age':30},{'name':'akhil','age':44},{'name':'sanu','age':18}]
for i in range(0):
    name=(input('name'))
    age=(int(input('age')))
    dtl.append({'name':name,'age':age})
print("{:<10}{:<6}".format("name","age"))
print('_'*20)
for i in dtl:
    print("{:<10}{:<6}".format(i['name'],i['age']))

print("age>30")
print("{:<10}{:<6}".format("name","age"))
for i in dtl:
    if i['age']>=30:
        print("{:<10}{:<6}".format(i['name'],i['age']))

print("age<30")
print("{:<10}{:<6}".format("name","age"))
for i in dtl:
    if i['age']<=30:
        print("{:<10}{:<6}".format(i['name'],i['age']))