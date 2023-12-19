class student:
    def __init__(self,name, roll_no,branch,contact):
        self.name=name
        self.roll=roll_no
        self.contact=contact
        self.branch=branch


    def printInfo(self):
        return f'the name of the student is {self.name} having roll number {self.roll} from branch {self.branch}, contact info : {self.contact}'
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

khushnam=student("khushnam",48,"MCA",879054689)
krishna=student.from_str("krishna-21-mca-986899765")
print(krishna.printInfo())
print(khushnam.printInfo())