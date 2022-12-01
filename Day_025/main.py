# # csv 미사용
# with open("\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_025\\weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)
# # csv 사용
# with open("\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_025\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import csv
import pandas

#pandas사용 
data = pandas.read_csv("\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_025\\weather_data.csv")
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()


# 온도 평균 값 구하기
aver = sum(temp_list) / len(temp_list)
print(aver)
# pandas의 mean으로 평균 값
print(data["temp"].mean())
# temp의 젤 높은 값
print(data["temp"].max())
#data를 columns로 부르기
print(data["condition"])
print(data.condition)
#행에서 데이터를 구하기
print(data[data.day == "Sunny"])
# 높은 온도를 가진 행 불러오기
print(data[data.temp == data["temp"].max()] )

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
mondey_temp = monday_temp *9/5 +32
print(mondey_temp)

# create a datafram form scratch
data_dict = {
    "student": ["Amy", "James","Angela"],
    "scores":[76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")