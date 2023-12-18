student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total=0
for height in student_heights:
  total+=height
# print(total)

students=0
for stud in student_heights:
  students+=1
# print(students)

average=round(total/students)
print("average height of students in the list is : ", average)