# # # # # # conditional statement in python
# # # # # number = int(input("Which number do you want to check? "))
# # # # # if number%2==0 :
# # # # #   print(f"{number} is a even number ")
# # # # # else :
# # # # #   print(f"{number}  is a odd number")

# # # # #rollercoaster program (nested if else)

# # # # print("welcome to roller coaster")
# # # # height = int(input("what is your height?? "))
# # # # if height >= 120:
# # # #   age = int(input("what is your age?? "))
# # # #   if age < 12:
# # # #     print("you have to pay 5$")
# # # #   elif age >= 18:
# # # #     print("you have to pay 18$")
# # # #   else:
# # # #     print("you have to pay 7$")
# # # # else:
# # # #   print(
# # # #       "you are not tall enough to ride this roller coaster come again later have a nice day.")

# # # height = float(input("enter your height in m: "))
# # # weight = float(input("enter your weight in kg: "))

# # # bmi= round(weight/height**2)
# # # if bmi<=18.5 :
# # #   print("you are underweight")
# # # elif bmi<25 :
# # #   print("you have normal weight")
# # # elif bmi<30 :
# # #   print("slighlty overweight")
# # # elif bmi<35 :
# # #   print("obese")
# # # elif bmi>35 :
# # #   print("clinically obese")

# # # to find a year
# # # year = int(input("Which year do you want to check? "))
# # # if (year % 100==0) and (year%100==0):
# # #   print("leap year.")
# # # elif (year% 100 !=0) and (year % 4==0) :
# # #   print("leap year.")
# # # else :
# # #   print("not leap year.")
Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
for making pizza odrering site
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "s":
  bill += 15
elif size == "m":
  bill += 20
elif size == "l":
  bill = +25

if add_pepperoni == "y":
  if size == "s":
    bill += 2
  else:
    bill += 3
if extra_cheese == "y":
  bill += 1

print(f"Your final bill is: {bill}$")

# # for friendship calculator
# from typing import Counter

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# combined = name1 + name2
# lower = combined.lower()
# t = lower.count("t")
# r = lower.count("r")
# u = lower.count("u")
# e = lower.count("e")
# true = t + r + u + e

# f = lower.count("f")
# d = lower.count("d")
# i = lower.count("i")
# e = lower.count("e")
# n = lower.count("n")
# friendship = f + n + i + e + d

# friendship_score = int(str(true) + str(love))
# if (friendship_score < 10) or (friendship_score > 90):
#   print(f"Your score is {friendship_score}, you go together like coke and mentos.")
# elif (40 < friendship_score < 50):
#   print(f"Your score is {friendship_score}, you are alright together.")
# else:
#   print(f"Your score is {friendship_score}.")


