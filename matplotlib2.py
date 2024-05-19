#You have two datasets: one containing the heights and another containing the weights of
 #individuals. Your task is to create a scatter plot using Matplotlib to visualize the relationship
 #between height and weight.
import matplotlib.pyplot as plt
 heights = [65, 68, 70, 62, 72, 69, 74, 61, 63, 66] # Heights in inches
 weights = [120, 150, 160, 110, 180, 140, 190, 105, 115, 125] # Weights in pounds
 plt.figure(figsize=(8, 6))
 plt.scatter(heights, weights, color='blue', marker='o')
 plt.title('Relationship between Height and Weight')
 plt.xlabel('Height (inches)')
 plt.ylabel('Weight (pounds)')
 plt.grid(True)
 plt.show()
