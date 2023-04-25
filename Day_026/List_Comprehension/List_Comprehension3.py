

with open("./List_Comprehension/file1.txt") as file:
    data_1 = file.readlines()
with open("./List_Comprehension/file2.txt") as file:
    data_2 = file.readlines()

data1 = [int(data.strip("\n")) for data in data_1]
data2 = [int(data.strip("\n")) for data in data_2]

result = [i for i in data1 if i in data2]

# Write your code above 👆

print(result)

