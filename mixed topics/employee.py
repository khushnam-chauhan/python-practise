class Employee:
    def __init__(self,name,age,designation,id,salary):
        self.name=name
        self.age=age
        self.designation=designation
        self.id=id
        self.salary=salary
    
    def set_incentive(self,incentive):
        self.incentive=incentive

    def total_salary(self):
        return self.salary + self.incentive
    
    def display_all(self):
        print(f"employee name - {self.name}")
        print(f"age - {self.age}")
        print(f"designation - {self.designation}")
        print(f"employee id - {self.id}")
        print(f"employee salary - {self.salary}")
        print(f"employee incentive - {self.incentive}")
        print(f"employee total salary - {self.total_salary()}")



dj=Employee("dhananjay",22,"software engineer",201,70000)
dj.set_incentive(5000)
dj.display_all()
prayas=Employee("prayas",22,"nalla",201,600000)
prayas.set_incentive(5100)
prayas.display_all()
