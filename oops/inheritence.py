#SINGLE INHERITENCE

class teacher:
    def textbook(s):
        print('read text')
    def note(s):
        print("note")
class student(teacher):
    def book(s):
        print('read a book')


anu=student()
anu.note()
vijaya=teacher()
vijaya.textbook()

#MULTIPLE INHERITENCE

class school:
    def __init__(self):
        print("register")
    def std(s):
        print("class")
class Class:
    def div(s):
        print('divition')
class student(Class,school):
    def book(s):
        print('read')
#multilevel

class school:
    def __init__(self):
        print("register")
    def std(s):
        print("class")
class Class(school):
    def div(s):
        print('divition')
class student(Class):
    def book(s):
        print('read')

#hierarchial

class school:
    def __init__(self):
        print("register")
    def std(s):
        print("class")
class Class(school):
    def div(s):
        print('divition')
class student(school):
    def book(s):
        print('read')


#hybrid 

class school:
    def __init__(self):
        print("register")
    def std(s):
        print("class")
class Class(school):
    def div(s):
        print('divition')

class teacher(school):
    def textbook(s):
        print("read")
class student():
    def book(s):
        print('read')

