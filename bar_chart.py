import matplotlib.pyplot as plt

product = ['mouse', 'keyboard', 'pendrive', 'ssd', 'ram']
sales = [3500, 2800, 1200, 5500, 4500]

plt.bar(product, sales, color='orange', label='Sales 2025')

plt.xlabel("Product", color='purple')
plt.ylabel("Sales", color='purple')

plt.title("Product sale comparison", color='blue')

plt.legend()

plt.show()