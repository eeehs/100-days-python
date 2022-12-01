import pandas,csv

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_Color_data_list = data["PrimaryFurColor"].to_list()

gray_count = 0
black_count = 0
red_count = 0 

for i in fur_Color_data_list:
    if i == "Gray":
        gray_count +=1
    elif i == "Black":
        black_count +=1
    elif i == "Cinnamon":
        red_count +=1
    else:
        pass
new_data = {
    "Fur Color":["gray","black","red"],
    "Count":[gray_count,black_count,red_count]
}
data = pandas.DataFrame(new_data)

data.to_csv("new_squirl.csv")
