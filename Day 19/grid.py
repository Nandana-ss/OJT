import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,2,3,4,5]

plt.plot(x, y1,label = "first plot",linestyle='-',color='r',linewidth=3, marker='*',markersize=8,markerfacecolor='g')
plt.plot(x, y2,label = "second plot",linestyle='--',color='b',linewidth=3, marker='x',markersize=8,markerfacecolor='yellow')
plt.title("customized line plot with grid")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.grid(color='grey',linestyle='--',linewidth='1')
plt.show()