##Watson gives Sherlock an array A1,A2...AN. 
##He asks him to find an integer M between P and Q(both inclusive), such that, min {|Ai-M|, 1 ≤ i ≤ N} is maximised. If there are multiple solutions, print the smallest one. 
##Input Format 
##The first line contains N. The next line contains space separated N integers, and denote the array A. The third line contains two space separated integers denoting P and Q. 
##Output Format 
##In one line, print the required answer.
##Constraints 
##1 ≤ N ≤ 102 
##1 ≤ Ai ≤ 109 
##1 ≤ P ≤ Q ≤ 109 
##Sample Input 
##3
##5 8 14
##4 9
##Sample Output   6 min[1 2 8]
##4
##Explanation 
##For M = 4,6,7, or 9, the result is 1. Since we have to output the smallest of the multiple solutions, we print 4.
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