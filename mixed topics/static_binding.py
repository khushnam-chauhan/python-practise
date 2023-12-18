class MathOperations:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

calculator = MathOperations()
result1 = calculator.add(2, 3)       # Calls the first add method
result2 = calculator.add(2, 3, 4)    # Calls the second add method
