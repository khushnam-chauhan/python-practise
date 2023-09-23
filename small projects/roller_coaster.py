 #rollercoaster program (nested if else)

print("welcome to roller coaster")
height = int(input("what is your height?? "))
if height >= 120:
   age = int(input("what is your age?? "))
    if age < 12:
        print("you have to pay 5$")
    elif age >= 18:
        print("you have to pay 18$")
    else:
        print("you have to pay 7$")
else:
print("you are not tall enough to ride this roller coaster come again later have a nice day.")
