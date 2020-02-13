from die import Die

import pygal

# 创建两个D6
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# 掷几次骰子，并将结果储存在一个列表中
results = [die_1.roll() * die_2.roll() * die_3.roll() for roll_num in range(1000000)]

# 分析结果
max_result = die_1.num_sides * die_2.num_sides * die_3.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [x for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
