num1=int(input("enter the two numbers to get the gcd /n"))
num2=int(input("enter 2 nd num : "))
if num1>num2:
    smaller=num2
else:
    smaller=num1
for i in range(1,smaller+1):
    if(num1%i==0)and(num2%i==0):
        gcd=i

print(f"the gcd of {num1} and {num2} is {gcd}.")
