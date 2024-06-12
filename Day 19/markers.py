import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [2,3,5,7,11,12,13]
plt.plot(x, y, marker='o', linestyle='-.',color='b',markersize=6,markerfacecolor = 'r')
plt.title("line plot with marker")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()