class Student:
    def __init__(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch

class Test(Student):
    def __init__(self,name,roll,branch,subject1, subject2):
        super().__init__(name,roll,branch)
        self.subject1=subject1
        self.subject2=subject2

class Result(Test):
    def average(self):
        return (self.subject1+self.subject2)/2

    def printer(self):
       print(f"student name : {self.name} have roll number {self.roll} from {self.branch} got {self.subject1} marks and {self.subject2} marks. getting the average of {self.average()} ")

 
dj=Result("dj",61,"cse",98,34)
dj.average()
dj.printer()