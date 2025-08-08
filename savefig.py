import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x, y, color='blue', marker='o')
plt.title("Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.savefig("mychart.png", dpi=300, bbox_inches='tight')