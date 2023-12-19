class Parent:
    def func1(self):
        print("this is parent class")

class child(Parent):
    def func2(self):
        print("this is child class")


obj=child()
obj.func2()
obj.func1()