# class A:
#     def __init__(s,name,age):
#         print("A class display method")
#         print(name,age)
#     def s1(s):
#         print("A class S1")
# class B(A):
#     def __init__(s,name,age):
#         print(name,age)
#         print("B class display method")
#         super().__init__(name,age)
#     def d1(s):
#         print("B class d1")

# obj=B('akhil',25)


#ABSTRACTION

# from abc import ABC,abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def make_sound(s):
#         print("sound")
# class bird(animal):
#     def fly(s):
#         print("fly")
#     def make_sound(s):
#         print("bird sound")
# class cat(animal):
#     def run(s):
#         print('run')
#     def make_sound(s):
#         print("cat sound")
# print('BIRD')
# b1=bird()
# b1.fly()
# b1.make_sound()
# print('CAT')
# c1=cat()
# c1.run()
# c1.make_sound()

#REGULAR EXPRESSION

# a='welcome'
# import re
# print(re.sub('w','W',a))
# print(re.sub('welcome','python',a))

# print(re.split('e',a,1))
# b=re.split('e',a)
# print(b)

# print(re.findall('e',a))
# print(len(re.findall('e',a)))

# print(re.search('e',a))
# if re.search('l',a):
#     print('yes')
# else:
#     print('no')
# print(re.search('[a-z]',a))
# a='Welcome'
# print(re.search('[A-Z]',a))
# a='welcome123'
# print(re.search('[0-9]',a))
# a='AbCd123'
# print(re.search('a.',a))
# print(re.search('b.',a))
# print(re.search('c.',a))
# print(re.search('d.',a))
# print(re.search('c..',a))
# print(re.search('c.*',a))
# print(re.search('c.+',a))
# print(re.search('c.?',a))print(re.search('a.',a))
# print(re.search('[A-Z].',a))
# print(re.search('[A-Z].',a))
# print(re.search('[A-Z].',a))
# print(re.search('[A-Z]..',a))
# print(re.search('[A-Z].*',a))
# print(re.search('[A-Z].+',a))
# print(re.search('[A-Z].?',a))
# print(re.search('[a-z].',a))
# print(re.search('[a-z].',a))
# print(re.search('[a-z].',a))
# print(re.search('[a-z]..',a))
# print(re.search('[a-z].*',a))
# print(re.search('[a-z].+',a))
# print(re.search('[a-z].?',a))
# print(re.search('[0-9].',a))
# print(re.search('[0-9].',a))
# print(re.search('[0-9].',a))
# print(re.search('[0-9]..',a))
# print(re.search('[0-9].*',a))
# print(re.search('[0-9].+',a))
# print(re.search('[0-9].?',a))


# import re
# a="AabCd123"
# print(re.search('[a-z][0-9]',a))
# print(re.search('[A-Z][a-z][0-9]',a))
# print(re.search('[A-Z][a-z][0-9][0-9]',a))
# print(re.search('[A-Z].*[a-z].*[0-9]',a))
# print(re.search('[a-z0-9]$',a))
# print(re.search('[0-9]$',a))
# B='Welcome'
# print(re.search('e$',B))
# print(re.search('Welcome$',B))


#PHONE NUMBER VALIDATION
# import re
# a=input('enter your number: ')
# if len(a)==10 and a.isdigit() and re.search('[6-9].{9}',a):
#     print("valid")
# else:
#     print("invalid")



# import re

# email = input('Enter your email address: ')

# # Regular expression pattern for validating email addresses
# pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# # Check if the email matches the pattern using re.match
# if re.match(pattern, email):
#     print("Valid email address")
# else:
#     print("Invalid email address")




#EMAIL VAILDATION
import re

email = input('Enter your email address: ')

if re.search('[a-z].*@gmail.com',email):
    print("Valid email address")
else:
    print("Invalid email address")
