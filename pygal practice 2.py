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
import math

line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)   #no need to show all x labels
line_chart.title = "closing price logged"

line_chart.x_labels = dates
N = 20   #show every 20 days
line_chart.x_labels_major = dates[::N]

close_log = [math.log10(i) for i in close]

line_chart.add("log closing price", close_log)
line_chart.render_to_file("line graph of logged closing price.svg")

from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key = lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list)/len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+".svg")
    return line_chart

idx_month = dates.index("2017-12-01")
line_chart_month = draw_line(months[:idx_month], close[:idx_month], "monthly average closing price", "monthly average")
line_chart_month

idx_week = dates.index("2017-12-11")
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], "weekly average closing price", "weekly average")
line_chart_week