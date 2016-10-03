//https://www.hackerrank.com/challenges/accessory-collection
import sys
import itertools
import math
L = []
A = []
N = []
D = []
final_list = []
T = int(input().strip())
if(T >= 1 and T <= pow(10,6)):
	for a0 in range(T):
		x,y,z,a = input().strip().split(' ')
		x,y,z,a = int(x),int(y),int(z),int(a)
		L.append(x)
		A.append(y)
		N.append(z)
		D.append(a)
else:
	raise SystemExit

def checkdistinct(subsetlist, D):
	for i in range(len(subsetlist)):
		temp = set(subsetlist[i])
		if (len(temp) < D):	
			return False
	return True

def appenditem(itemlist, Alist , N , D):
	if (len(itemlist) == 0 ):
		itemlist.append(max(Alist))
	else:
		for item in Alist:
			temp = []
			temp = itemlist[:]
			temp.append(item)
			if(len(temp) > N ):
				subsetlist = [x for x in list(itertools.combinations( temp, N))]
				flagcheck = checkdistinct(subsetlist ,D)
				if(flagcheck):
					itemlist.append(item)
					break
				else:
					continue
			elif(len(temp) == N):
				if(len(set(temp)) >= D):
					itemlist.append(item)
					break
			else:
				itemlist.append(item)
				break

for i in range(T):
	if( D[i] >=1 and D[i] <= pow(10,5) and N[i] >=1 and N[i] <= pow(10,5) and  L[i]>=1 and L[i] <= pow(10,5) and A[i] >= 1 and A[i] <= pow(10,9) and sum(L) <= 8*pow(10,6)):
		Alist = [x for x in range(1,(A[i]+1))]
		Alist = sorted(Alist, reverse = True )
		if (A[i] < D[i]):
			final_list.append([])
			continue
		itemlist = []
		for j in range(0,L[i]):
			appenditem(itemlist,Alist , N[i], D[i])
		final_list.append(itemlist)
	else:
		raise SystemExit

			
for li in final_list:
	if(len(li) == 0):
		print("SAD")
	else:
		print(sum(li))
