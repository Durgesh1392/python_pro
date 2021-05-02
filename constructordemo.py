class Student:
    def __init__(self):
        print("constructor executed")

    def m(self):
        print(" method executed")

s1 = Student()
s2 = Student()
s3 = Student()
s1.m()
s2.m()