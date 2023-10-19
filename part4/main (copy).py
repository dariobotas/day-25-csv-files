""" How to use pandas (simple way)"""
import pandas


if __name__ == "__main__":
  data = pandas.read_csv("part4/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
  #print(data_squirrel)

  #challenge 1 - count each colors of Primary Fur Color and export to new csv file
  color_data = data["Primary Fur Color"]
  
  all_colors = color_data.unique()
  squirrel_count = {
    "Fur Color": [],
    "Count": []
  }
  
  for color in all_colors:
    squirrel_count["Fur Color"].append(color)
    squirrel_count["Count"].append(len(data[color_data == color]))
    #print(f"len(data[color_data == color])")

  new_csv_file = pandas.DataFrame(dict(squirrel_count))
  print(new_csv_file)
  new_csv_file.to_csv("part4/squirrel_count.csv")

""" Instructor solution"""
data = pandas.read_csv("part4/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("part4/squirrels_count.csv")