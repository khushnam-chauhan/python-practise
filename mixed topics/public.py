class MyClass:
    def __init__(self):
        self.public_variable=10
        self._protected_variable=20
        self.__private_variable=30
    def public_method(self):
        print("this is a public method")
    def _protected_method(self):
        print("this is a protected method")
    def __private_method(self):
        print("this is a private method")

obj=MyClass()
print(obj.public_variable)
obj.public_method
print(obj._protected_variable)
obj._protected_method
print(obj._MyClass__private_variable)
obj._MyClass__private_method


