""" How to use pandas (simple way)"""
import pandas


if __name__ == "__main__":
  data = pandas.read_csv("part2/weather_data.csv")
  #print(type(data))
  #print(type(data["temp"]))

  data_dict = data.to_dict()
  #print(data_dict)

  data_list = data["temp"].to_list()
  #print(data_list)

  #challenge 1 - calculate mean temperature
  #print()
  #easy way
  #print(data["temp"].mean())
  #medium way
  average = sum(data_list) / len(data_list)
  #print(average)

  #challenge 2 - max temperature
  #print()
  #print(data["temp"].max())

  #get data in columns
  #print()
  #print(data["condition"])
  #print(data.condition)

  #get data in row
  #print(data[data.day == "Monday"])
  #print()
  #challenge 3 - max temperature data in row
  #print(data[data.temp == data.temp.max()])

  monday = data[data.day == "Monday"]
  #print(monday.condition)
  # challenge 4 - convert ºC fo ºF
  monday_temp = monday.temp[0] # shows only the value of 12 - without [0] is: 0   12
  #print(monday_temp)
  monday_temp_F = monday_temp * 9/5 + 32
  #print(monday_temp_F)
  
  #create a dataframe from scratch
  data_dict = {
    "student": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
  }
  data = pandas.DataFrame(data_dict)
  print(data)
  data.to_csv("part3/new_data.csv")