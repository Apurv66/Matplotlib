import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West']
revenue = [6700, 1200, 2000, 3200]

plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=['gold', 'skyblue', 'lightgreen', 'coral'])

plt.title("Revenue Contribution By Region")

plt.show()