
#Question No 01:
#Create the csv file named as ai_lab.csv. Add the following data in csv:
# Dothe following operations in python using pandas:
#1. Read above csv file as a dataframe.
#2. Calculate the mean values for Goals, Assists, and Yellow Cards. Also, print them on
#console.
#Code:
 import pandas as pd
 df = pd.read_csv('C:\\Users\\ladla\\OneDrive\\Desktop\\python\\ai_lab.csv')
 print(df)
 mean_goals = df['goals'].mean()
 mean_assists = df['assists'].mean()
 mean_yellow_cards = df['yellow cards'].mean()
 print("Mean Goals:", mean_goals)
 print("Mean Assists:", mean_assists)
 print("Mean Yellow Cards:", mean_yellow_cards)
##Output:
 #3. Replace the missing values for each column with their respective column’s mean
# value.
# 4. Now, again calculate the mean for each column. Add Assist’s column mean value
 #and
# Yellow Card’s column mean value. Finally, subtract that addition result from the
 #mean
 #value of Goals column. See formula:
# result = mean_of_Goals– (mean_of_Assists + mean_of_Yellow_Cards)
# 5. Now, export the final dataframe into csv file, named as final.csv.
#Code:
 import pandas as pd
 df = pd.read_csv('C:\\Users\\ladla\\OneDrive\\Desktop\\python\\ai_lab.csv')
 print(df)
 mean_goals = df['goals'].mean()
 mean_assists = df['assists'].mean()
 mean_yellow_cards = df['yellow cards'].mean()
 print("Mean Goals:", mean_goals)
 print("Mean Assists:", mean_assists)
 print("Mean Yellow Cards:", mean_yellow_cards)
 df['goals'].fillna(mean_goals, inplace=True)
 df['assists'].fillna(mean_assists, inplace=True)
 df['yellow cards'].fillna(mean_yellow_cards, inplace=True)
 print(df)
 result = mean_goals- (mean_assists + mean_yellow_cards)
 print("Result:", result)
 df.to_csv('C:\\Users\\ladla\\OneDrive\\Desktop\\python\\final.csv', index=False)
 print("Final dataframe has been exported to final.csv")
 #Output:
#QUESTION NO2:
 #Use matplotlib and pandas in python to create graphs as follow:
# a) Read csv file in Question (1), using pandas, as a dataframe
# b) Create the line graph for Players (x-axis) and Yellow Cards (y-axis)
 #Code:
# c) Draw scatter plot for Players (x-axis) and Assists (y-axis)
 #d) Finally, plot the bar graph for Country (x-axis) and Goals (y-axis)
 #Code:
 import pandas as pd
 import matplotlib.pyplot as plt
 df = pd.read_csv('C:\\Users\\ladla\\OneDrive\\Desktop\\python\\final.csv')
 plt.figure(figsize=(10, 6))
 plt.plot(df['Players'], df['Yellow Cards'], marker='o', color='orange')
 plt.title('Yellow Cards per Player')
 plt.xlabel('Players')
 plt.ylabel('Yellow Cards')
 plt.xticks(rotation=90)
 plt.grid(True)
 plt.tight_layout()
 plt.show()
 plt.figure(figsize=(10, 6))
 plt.scatter(df['Players'], df['Assists'], color='green')
 plt.title('Assists per Player')
 plt.xlabel('Players')
 plt.ylabel('Assists')
 plt.xticks(rotation=90)
 plt.grid(True)
 plt.tight_layout()
 plt.show()
 plt.figure(figsize=(10, 6))
 plt.bar(df['Country'], df['Goals'], color='blue')
 plt.title('Goals by Country')
 plt.xlabel('Country')
 plt.ylabel('Goals')
 plt.xticks(rotation=45)
 plt.grid(True)
 plt.tight_layout()
 plt.show()
