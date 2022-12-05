# number =[ 1,2,3]
# new_list = []
# for n in list:
#     add_1 = n + 1
# new_list.append(add_1)

# new_list = [n+1 for n in numbers]


numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]

print(new_list)

range_list = [n*2 for n in range(1,5)]

print(range_list)

names = ['Alex','beth','caroline','dave','elanor','freddie']

short_names =[name.upper() for name in names if len(name)>=5]
print(short_names)

# Challenge 1 
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [number*number for number in numbers]
#Write your code 👆 above:

print(squared_numbers)

# Challenge 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
result = [num for num in numbers if num % 2 ==0]
#Write your code 👆 above:

print(result)

# Challenge 3

# Write your code above 👆

with open(".\\Day_026\\file1.txt") as file:
    file1_list = [int(i.strip()) for i in file.readlines()]
with open(".\\Day_026\\file2.txt") as file:
    file2_list = [int(i.strip()) for i in file.readlines()]
result = [i for i in file1_list if i in file2_list]
print(result)
