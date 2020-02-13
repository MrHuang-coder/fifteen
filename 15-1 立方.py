import matplotlib.pyplot as plt

input_values = list(range(1, 1001))
cube = [x**3 for x in input_values]
plt.scatter(input_values, cube, c=cube, cmap=plt.cm.Reds, linewidth=8)

# 设置图表标题, 并给坐标轴加上标签
plt.title("cube Numbers", fontsize=25)
plt.xlabel("Value", fontsize=15)
plt.ylabel("cube of Value", fontsize=15)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000000])
plt.show()
