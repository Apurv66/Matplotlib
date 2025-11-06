import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Batsman': ['R Sharma', 'S Gill', 'V Kohli', 'KL Rahul', 'S Iyer', 'A Patel', 'W Sundar'],
    'Runs': [73, 9, 5, 11, 61, 44, 12]
}

df = pd.DataFrame(data)

plt.pie(df['Runs'], labels=df['Batsman'], colors=['royalblue', 'coral', 'red', 'lightgreen', 'slateblue', 'aqua', 'orange'], explode=[0,0.08,0,0,0,0,0], shadow=True)
plt.title("Run Contribution Analysis (IND vs AUS)")
plt.show()