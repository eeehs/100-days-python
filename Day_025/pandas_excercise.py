# import csv
# import pandas

# # with open("./Day_025/weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] == "temp":
# #             pass
# #         else:
# #             temperatures.append(int(row[1]))
    
# data = pandas.read_csv("./Day_025/weather_data.csv") 

# data_dict = data.to_dict()

# tem_list = data["temp"].to_list()

# # print(data["temp"].mean())

# # print(data[data.temp == data.temp.max()])

# tem_list = data.temp.to_list()
# print(tem_list)

# # Create Dataframes from scratch

# data2 = pandas.DataFrame(data_dict)

import pandas

data = pandas.read_csv("Day_025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sqirrels_count = len(data["Primary Fur Color"] == "Gray")
red_sqirrels_count = len(data["Primary Fur Color"] == "Cinnamon")
black_sqirrels_count = len(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon","Black"],
    "Count": [grey_sqirrels_count,red_sqirrels_count,black_sqirrels_count ]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("Day_025/squirrel_count.csv")