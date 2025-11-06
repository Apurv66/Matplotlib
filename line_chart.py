import matplotlib.pyplot as plt
import pandas as pd
data = {
    'year': [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
    'virat': [308, 302, 345, 505, 490, 390, 634, 601],
    'rohit': [288, 325, 378, 408, 365, 507, 439, 512]
}

df = pd.DataFrame(data)

plt.plot(df['year'], df['virat'], color='red', linestyle='dashed', marker='>', label='Virat')
plt.plot(df['year'], df['rohit'], color='blue', linestyle='dashdot', marker='o', label='Rohit')
plt.title("Virat vs Rohit Run Comparasion (2008 - 2015)")
plt.xlabel("Year")
plt.ylabel("Runs")
plt.grid()
plt.legend()
plt.show()