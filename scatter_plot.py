import matplotlib.pyplot as plt
import pandas as pd

data = {
    'batter': ['V Kohli', 'R Sharma', 'S Dhavan', 'D Warner', 'MS Dhoni', 'R Dravid', 'S Tendulkar', 'A Russal'],
    'Avg': [51, 45, 55, 47, 43, 55, 57, 38],
    'SR': [144.8, 152.3, 139.9, 148.3, 152.9, 122.5, 122.3, 172.1]
}

df = pd.DataFrame(data)

plt.scatter(df['Avg'], df['SR'], color='red')
plt.title("Average and Strike Rate Analysis")
plt.xlabel("Average")
plt.ylabel("Strike Rate")
plt.grid()
plt.show()