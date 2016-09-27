import sys
import math
N = 0
A =[]
P = 0 
Q =0
m= 1
import sys
data = sys.stdin.readline().rstrip()
N = int(data)
if(N <= 0 or N >= pow(10,2)):
	print("please provide correct N")
	raise SystemExit
data2 = sys.stdin.readline().rstrip()
temp = data2.split(" ")
for i in range(len(temp)):
	if(int(temp[i]) <= 0 or int(temp[i]) >= pow(10,9) ):
		print("please enter correct value for array")
		raise SystemExit
	else:
		A.append(int(temp[i]))
data3 = sys.stdin.readline().rstrip()
temp1 = data3.split(" ")
if(int(temp1[0]) <= 0 or int(temp1[0]) >= pow(10,9) or int(temp1[1]) <= 0 or int(temp1[1]) >= pow(10,9) ):
	print("please enter correct value for P and Q")
	raise SystemExit
else:
	P = int(temp1[0])
	Q = int(temp1[1])
A.sort()
if P > Q :
	PQList = list(range(Q,P+1))
else:
	PQList = list(range(P,Q+1))
#print(PQList)
#print(A)
#print(N , A , P , Q)
minitemlist = {}
def minfind():
	for M in PQList:
		templist = []
		for ai in A:
			templist.append(abs(ai - M))
		minitemlist[M] = min(templist)
		#print(minitemlist)
	#print(minitemlist)
	return(max(minitemlist, key=minitemlist.get))
print(minfind())
#print(minitemlist[0])
