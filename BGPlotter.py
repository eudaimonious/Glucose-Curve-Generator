from matplotlib import pyplot, mlab, ticker

data = mlab.csv2rec("BGData1.csv", delimiter='\t')
x_values = data.time
y_values = data.bg

fig, ax = pyplot.subplots()
# ax.xaxis_date() This has no bearing on the output
fig.autofmt_xdate()



pyplot.plot(x_values, y_values, "o-")

pyplot.ylabel("Blood Sugar Readings")
pyplot.xlabel("Time")
pyplot.title("Shoutao's Glucose Curve")

pyplot.show()