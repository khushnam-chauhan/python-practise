print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path1 = input("choose where you want to go. left or right\n")
path1_1 = path1.lower()
if path1_1 == "right":
  print("your luck ends there was a lion and u got eaten .\n")
elif path1_1 == "left":
  print("you can proceed there was a gold coin\n")
path2 = input("choose water or fire\n")
path2_2 = path2.lower()
if path2_2 == "water":
  print("you died because you don't have swimming skills\n")
elif path2_2 == "fire":
  print(
      "there was a fire but it was extinguished by the water flow so you save to proceed u got 10 gold coins\n"
  )
path3 = input("choose a color blue, white\n")
path3_3 = path3.lower()
if (path3_3 == "blue"):
  print("you died there were sharks bad luck\n")
elif (path3_3 == "white"):
  print("you won congrats you lucky fellow you won the treasure\n")
else:
  print("your input was invalid try again.")
