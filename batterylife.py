from sklearn_linearmodel import LinearRegression
import sys
import math
f = read_csv("temp.txt")
data = []
for line in f :
	temp = (line.split(","))
	temp1 = int(temp[0])
	temp2 = int(temp[1])
	templist = [temp1, temp2]
	data.append(templist)
lr = LinearRegression()
data_train = data[:-20,]
data_test = data[-20:,]
lr.fit(data_train[,0], data_train[,1])
coeff = lr.coef_
intercept = lr.intercept_
data = float(sys.stdin.readline())
sumofsquares = 0.0
def leastsquaresontest():
	for i in range(len(data_test)):
		predicted_value = predict(coeff , data_test[i,0], intercept)
		sumofsquares += math.pow(predicted_value,2) - math.pow(data_test[i,1])
	return sumofsquares
def predict(coeff, data , intercept):
	return round((coeff*data + intercept) , 2)


data = float(sys.stdin.readline())
print(predict())
