import matplotlib.pyplot as plt
import pandas as pd
from re import sub
from decimal import Decimal

data = pd.read_csv('data.csv')

print(list(data.columns.values))

x = str(input("Select the x-axis variable "))
y = str(input("Select the y-axis variable "))

type = str(input("Type of graph? Scatterplot(Type S) "))

remove_nan = data.dropna(subset=[x, y])

def value_to_float(x):
    if 'K' in x:
        if len(x) > 1:
            return (float(x.replace('€', '').replace('K', ''))) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return (float(x.replace('€', '').replace('M', ''))) * 1000000
        return 1000000.0
    if 'B' in x:
        return (float(x.replace('€', '').replace('B', ''))) * 1000000000
    return 0.0


if remove_nan[x].dtype == 'O':
	clean_data_x = remove_nan[x].map(value_to_float, axis=1)
else:
	clean_data_x = remove_nan[x]

if remove_nan[x].dtype == 'O':
	clean_data_y = remove_nan[y].map(value_to_float, axis=1)
else:
	clean_data_y = remove_nan[y]

if type == 'S':
	plt.scatter(clean_data_x, clean_data_y, c="r")
	plt.title("%s against %s" % (x,y))
	plt.xlabel(x)
	plt.ylabel(y)
	plt.gca().invert_yaxis()
	plt.show()
	corr_cof = clean_data_x.corr(clean_data_y)
	if (abs(corr_cof) > 0.7):
		print("There is a strong correlation between %s and %s" % (x, y))
	else:
		print("There is a weak correlation between %s and %s" % (x, y))

input()





