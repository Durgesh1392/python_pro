

class Student:
    """Developed for oops concept demo"""
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def talk(self):
        print("my name is ",self.name)
        print("my age is ",self.age)
        print("my marks are ",self.marks)
# if __name__ == '__main__':

s1= Student('durgesh', 28, 80)
s1.talk()