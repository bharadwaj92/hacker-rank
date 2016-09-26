from sklearn_linearmodel import LinearRegression
import sys
f = read_csv("temp.txt")
data = []
for line in f :
	data.append(line.split(","))
lm = LinearRegression()
lm.fit(data[,0], data[,1])
coeff = lr.coef_
intercept = lr.intercept_
data = float(sys.stdin.readline())
print(predict())

def predict(coeff, data , intercept):
	return round((coeff*data + intercept) , 2)
