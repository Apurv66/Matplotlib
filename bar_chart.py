import matplotlib.pyplot as plt
import pandas as pd

data= {
    'Batsman': ['R Sharma', 'V Kohli', 'S Dhavan', 'MS Dhoni', 'D Warner', 'S Raina'],
    '2016': [489, 973, 501, 284, 848, 399],
}

df = pd.DataFrame(data)

plt.bar(df['Batsman'], df['2016'], color=['blue', 'red', 'orange', 'yellow', 'orange', 'darkorange']) # plt.barh() for Horizontal Bar Chart
plt.title('2016 Season Runs Analysis')
plt.xlabel('Batsman')
plt.ylabel('2016')
plt.grid()
plt.show()