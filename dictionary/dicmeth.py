d={'name':'anu','age':20}

print(d.get("name"))

print(d.items())

for i,j in d.items():
    print(i)
    print(j)

print(d.keys())
print(d.values())
# print(d.pop('age'))
# print(d.popitem())
print(d.setdefault("place"))
print(d)

print(d.update({"place":"ekm"}))
print(d)

l=[1,2,3,4]
d1=d.fromkeys(l)
print(d1)
t=d.copy()
print(t)