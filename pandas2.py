#Use open source sites to download any dataset n csv format. Read that csv in python and
 #display all the information regarding that dataset (head, tail, shape etc.). After that, calculate
 #mean for every numerical column present
import pandas as pd
 df = pd.read_csv('C:\\Users\\ladla\\OneDrive\\Desktop\\python\\new.csv')
 print("Head of the dataset:")
 print(df.head())
 print("\nTail of the dataset:")
 print(df.tail())
 print("\nShape of the dataset:")
 print(df.shape)
 numerical_columns_mean = df.mean()
 print("\nMean for every numerical column:")
 print(numerical_columns_mean)
