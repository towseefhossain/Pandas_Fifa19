import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv') #reading the CSV Data File

print(list(data.columns.values)) #Producing the list of variables the user can choose 

x = str(input("Select the x-axis variable ")) #Choosing the firse variable
type = str(input("Type of graph? Scatterplot(Type S) Pie Chart (Type P) Distribution Histogram (Type H) Bar Chart of Top 10 (Type B) ")) #Type of data visualization

if type == 'P': #code to output Pie Charts
	plt.pie(data[x].value_counts(), labels=data[x].value_counts().index)
	plt.show()

if type == 'H': #code to output Histograms
	plt.hist(data[x])
	plt.show()
	print("The mean %s of players in FIFA 19 is %s" % x, data[x].values.mean())
	print("The median %s of players in FIFA 19 is %s" % x, data[x].values.median())
	print("Most players in FIFA 19 have a %s of %s" % x, data[x].values.mode()[0])


if type == 'S': #code to output Scatterplots
	y = str(input("Select the y-axis variable ")) #Asking user for y-axis variable for the scatterplot
	plt.scatter(data[x], data[y], c="r")
	plt.title("%s against %s" % (x,y))
	plt.xlabel(x)
	plt.ylabel(y)
	plt.gca().invert_yaxis()
	plt.show()
	corr_cof = x.corr(y)
	if (abs(corr_cof) > 0.7):
		print("There is a strong correlation between %s and %s" % (x, y))
	else:
		print("There is a weak correlation between %s and %s" % (x, y))

if type == 'B': #code to output BarCharts
	plt.bar(data[x].value_counts().head(10).index, data[x].value_counts().head(10).values)
	plt.show()

input()





