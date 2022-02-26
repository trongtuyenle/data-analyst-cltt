import pandas as pd
import matplotlib.pyplot as plt

load_data = pd.read_csv("profit-from-return-orders.csv", header=0, sep=",")

# get values of 'sum_profit' to draw graph on x-axis
profit = load_data['profit']

# convert values of column 'sum_profit' to series
profit_series = pd.Series(profit)

# get label for y-axis from 'Sub_Category'
y_labels = load_data['sub_category']

# plot figure
plt.figure(figsize=(10,8))
ax = profit_series.plot(kind='barh')
ax.set_title('Profit from Returned Orders')
ax.set_xlabel('Profit')
ax.set_ylabel('Sub_Category')
ax.set_yticklabels(y_labels) # create tick for labels of y-axis
ax.set_xlim(-5000, 12000) # set x-axis cho rong hon - de nhin

rects = ax.patches # vá những cái barh với những labels của y-axis lại với nhau

# for each barh: place a label
for rect in rects:
	# Get X and Y placement of label from 'rect' variable
	# placement -> vị trí
	x_value = rect.get_width()
	y_value = rect.get_y() + rect.get_height() / 2

	# Number of points between bar and label. Change to your liking
	space = 5
	# Vertical alignment for positive values
	ha = 'left'

	# If value of bar is negative: Place label left of bar
	if x_value < 0:
		# Invert space to place label to the left
		# invert space -> đảo ngược ko gian
		space *= -1
		# Horizontally align label at right
		ha = 'right'

	# Use X value as label and format number with two decimal place
	label = "{:.2f}".format(x_value)

	# Create annotation
	plt.annotate(
		label,                      # Use `label` as label
		(x_value, y_value),         # Place label at end of the bar
		xytext=(space, 0),          # Horizontally shift label by `space`
		textcoords="offset points", # Interpret `xytext` as offset in points -> độ lệch theo điểm
		va='center',                # Vertically center label
		ha=ha)                      # Horizontally align label differently for
									# positive and negative values

plt.savefig("returned-orders-profit-for-sub-category.png")
#plt.show()