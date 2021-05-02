# Don't wait to start something for fear of not being good at it.
#
# You probably won't be good at it. But, you'll never get good if you don't start.
#
# There's beauty in not knowing and infinite potential in the beginner's mindset.
#
# If you're compelled to do something, just start and see where it leads.
#
# It might be magnificent.
class Student:
    def __init__(self):
        self.name = 'durgesh'
        self.age = 18
        self.marks = 80

    def talk(self):
        print("my name is",self.name)
        print("my age is",self.age)
        print("my marks are",self.marks)

if __name__ == '__main__':
    s = Student()
    s.talk()