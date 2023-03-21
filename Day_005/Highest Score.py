student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest = student_scores[0]
for maxx in student_scores:
    if maxx >= highest:
        highest = maxx

print(f"The hihhest score is {highest}")