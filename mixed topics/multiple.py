class Mother:
    mother_name=""
    def mother(self):
        print(self.mother_name)


class Father:
    father_name=""
    def father(self):
        print(self.father_name)

class son(Mother,Father):
    def print_parents(self):
        print(f"mother name = {self.mother_name}")
        print(f"father name = {self.father_name}")


s1=son()
s1.mother_name="sita"
s1.father_name="ram"
s1.print_parents()
