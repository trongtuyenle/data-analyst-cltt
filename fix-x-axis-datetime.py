import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

load_data = pd.read_csv('trend-line-sales.csv', header=0, sep=",")

load_data['Order_Date'] = pd.to_datetime(load_data['Order_Date'])

date = load_data['Order_Date']
values = load_data['sum(Sales)']

fig, ax = plt.subplots(figsize=(8, 6))

half_year_locator = mdates.MonthLocator(interval=6)
year_month_formatter = mdates.DateFormatter("%Y-%m")

# set up date
ax.xaxis.set_major_locator(half_year_locator)
ax.xaxis.set_major_formatter(year_month_formatter)
ax.plot(date, values)

# xoay xeo label year-month
fig.autofmt_xdate()

#plt.savefig("sales-for-each-month.png")
plt.show()