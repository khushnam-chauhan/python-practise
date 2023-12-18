# # # # randomization or simply randomness
# # # import random

# # # random_num = random.randint(1, 15)
# # # print(random_num)
# # # # if u want to print random float num u can use random functon where its always range from 0 to 1 but not includes 1
# # # random_float = random.random()
# # # print(random_float)

# # # random_float = random.random(1.0, 5.0)
# # # print(random_float)

# # #for splitting the list by any special cahracter use list name.split(",") it means list will be splitte dwhere it find (,) commas

# # import random
# # names_string = input("Give me everybody's names, separated by a comma. ")
# # names = names_string.split(", ")
# # leng=int(len(names))
# # print(leng)
# # rand=random.randint(0,leng-1)
# # print(f"{names[rand]} is going to pay todays bill")

# #mapping game with row and column
# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")