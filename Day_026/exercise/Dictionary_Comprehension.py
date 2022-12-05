import random
names = ['Alex','beth','caroline','dave','elanor','freddie']

student_score = {student:random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score)in student_score.items() if score >=60}

print(passed_students)

# Challenge 1 
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
sentence_list = sentence.split()
# result = {sen:len(sentence) for sentence in sentence_list}
result = {sentence:len(sentence) for sentence in sentence_list}
# print(result)
print(result)

# Challenge 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:

weather_f = {weekend:((f*9/5)+32) for (weekend,f) in weather_c.items() }


print(weather_f)