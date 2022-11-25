# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# len말고 총 리스트 갯수 세는 방법

student_len = 0
student_sum = 0


for A in student_heights:
    student_sum = student_sum + A 
    student_len = student_len + 1

Average_Height = round(student_sum / student_len)

print(Average_Height)




# sum 말고 총 합 더하는 방법