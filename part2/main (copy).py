#1st - import csv
import pandas


if __name__ == "__main__":
  #1st challenge
  #with open("part2/weather_data.csv", mode="r") as weather_data_file:
    #data = weather_data_file.readlines()
    #print(data)
  #with open("part2/weather_data.csv", mode="r") as weather_data_file:
    #data= csv.reader(weather_data_file)
    #2nd challenge
    #temperatures = []
    #for row in data:
    #  if row[1] != "temp":
    #    temperatures.append(int(row[1]))
    #  print(row)
    #print(temperatures)

  #3rd
  data = pandas.read_csv("part2/weather_data.csv")
  print(data)
  print(data["temp"])