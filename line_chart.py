import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000, 1500, 1200, 1800]

# color, linestyle, linewidth, marker and label are optional
plt.plot(months, sales, color="purple", linestyle='--', linewidth=2, marker='o', label='2025 sales data')

plt.xlabel("Months")
plt.ylabel("Sales")

plt.title("Monthly Sales Data")

plt.legend()

plt.grid(color="gray", linestyle=':', linewidth=1)

plt.xlim(1, 4)
plt.ylim(0,2000)

plt.xticks([1,2,3,4], ['January', 'February', 'March', 'April'])

plt.show()