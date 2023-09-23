# # # num=len(input("whats your name?\n"))
# # # # if you want to know what type of data type u have then use type() function
# # # print(type(num))
# # # # u can't print integer with strings,example
# # # # print("your name has"+num+" "+"characters")

# # # # so u have to convert your int to string
# # # # convert num to string
# # # new_num=str(num) #u can change type of data to any other data type like this
# # # # now u can run it
# # # print("your name has "+new_num+" "+"characters")

# # # # # qs to add 2 digit no. to each other like 23, 2+3=5
# # # # two_digit_number = input("Type a two digit number: ")
# # # # first=two_digit_number[0]
# # # # second=two_digit_number[1]
# # # # print(int(first)+int(second))

# # #f-string changing data types again and again can be painful so we use f-string to deal with it
# # #cause every variable should have same data type
# # score =0
# # height=1.7
# # iswinning=True

# # # print("your score is "+score+" ")
# # #but here we have float and str which can't be together so we use f-string
# # print(f"your score is {score},your height is {height},your are winning is {iswinning}")

# #this program will tell you how much time u have left in a span of 90 years of ur life
# age = input("What is your current age? ")
# days = 90 * 365 - int(age) * 365
# weeks = 90 * 52 - int(age) * 52
# month = 90 * 12 - int(age) * 12
# print(f"you have {days} days ,{weeks} weeks ,{month} months left ")

# #tip calculator

print("welcome to the tip calculator\n")

bill = input("what was the total bill??")
tip = input("what percentage of tip would you like to give?? ")
split = input("how many people to split the bill?? ")
percentage = float(bill) * float(tip) / 100
total_bill = (float(bill) + float(percentage)) / int(split)

print("each person should pay : " + format(total_bill, ".2f"))
