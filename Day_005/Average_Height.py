
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
number = 0
for student in student_heights:
    total += student
    number += 1
average = round(total / number)

print(average)