import pandas as pd
import matplotlib.pyplot as plt

# part - 1
df = pd.read_csv('final.csv')

# part - 2
x = df['Player Name'].tolist()
y = df['Yellow Cards'].tolist()
plt.plot(x, y, color='purple', marker='*', markersize=10)
plt.xlabel('Players Name')
plt.ylabel('Yellow Cards')
plt.title('Players with their Yellow Cards')
plt.xticks(rotation=45)
plt.show()


# part - 3
x = df['Player Name'].tolist()
y = df['Assists'].tolist()
plt.scatter(x, y, color='red')
plt.xlabel('Players Name')
plt.ylabel('Assists')
plt.title('Players with their Assists')
plt.xticks(rotation=45)
plt.show()



# part - 4
x = df['Country'].tolist()
y = df['Goals'].tolist()
plt.bar(x, y, color='green')
plt.xlabel('Country')
plt.ylabel('Goals')
plt.title('Countires with their Goals')
plt.xticks(rotation=45)
