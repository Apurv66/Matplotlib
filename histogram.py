import matplotlib.pyplot as plt
import pandas as pd

data = {
    'scores':[45,67,84,35,78,94,78,87,72,82,55,63,42]
}

df = pd.DataFrame(data)

plt.hist(df['scores'], bins=5, color='lightgreen', edgecolor='black')

plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.title("Score Distribution of Student")
plt.show()