import pandas as pd

# part - 1
df = pd.read_csv('players.csv')

# part - 2
mean1 = df['Goals'].mean()
mean2 = df['Assists'].mean()
mean3 = df['Yellow Cards'].mean()
print(mean1, '\n', mean2, '\n', mean3)

# part - 3
df['Goals'].fillna(mean1, inplace=True)
df['Assists'].fillna(mean2, inplace=True)
df['Yellow Cards'].fillna(mean3, inplace=True)

# part - 4
mean_goals_updated = df['Goals'].mean()
mean_assists_updated = df['Assists'].mean()
mean_yellow_cards_updated = df['Yellow Cards'].mean()

result = mean_goals_updated - (mean_assists_updated + mean_yellow_cards_updated)

# part - 5
df.to_csv('final.csv')