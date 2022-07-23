import json

filename = "btc_close_2017.json"
with open(filename) as f:
    btc_data = json.load(f)

dates, months, weeks, weekdays, close = [], [], [], [], []

for btc_dict in btc_data:
    dates.append(btc_dict["date"])
    months.append(btc_dict["month"])
    weeks.append(btc_dict["week"])
    weekdays.append(btc_dict["weekday"])
    close.append(int(float(btc_dict["close"])))

import pygal
line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)   #no need to show all x labels
line_chart.title = "closing price"
line_chart.x_labels = dates
N = 20   #show every 20 days
line_chart.x_labels_major = dates[::N]
line_chart.add("closing price", close)
line_chart.render_to_file("line graph of closing price 2.svg")
