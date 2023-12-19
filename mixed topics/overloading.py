class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    
calc=calculator()
result1=calc.add(1,2)
result2=calc.add(1,2,3)

print(result1)
print(result2)