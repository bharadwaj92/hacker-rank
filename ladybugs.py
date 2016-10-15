#https://www.hackerrank.com/contests/w24/challenges/happy-ladybugs
#!/bin/python3
import string
import sys
def checkladybugs(n,b,dict):
	if(len(dict.keys()) == 1):
		flag = True
		return flag
	if('_' in dict.keys()):
		for item in dict.keys():
			if(item == '_'):
				continue
			elif(dict[item] >=2):
				flag = True					
			else:
				flag = False
				break
		return flag
	else:
		for item in dict.keys():
			if(dict[item] >=2):
				flag = True
				continue
			else:
				flag = False
				return flag
		for i in range(n):
			if(i == 0):
				if(b[0] == b[1]):
					flag = True
					continue
				else:
					flag = False
					return flag
			else:
				if(b[i] == b[i-1] or b[i] == b[i+1]):
					flag = True
					continue
				else:
					flag = False
					return flag
		return flag
Q = int(input().strip())
if( Q < 1 or Q > 100):
	raise SystemExit
for a in range(0,2*Q-1 ):
	dict = {}
	flag = False
	min = 1
	n = int(input().strip())
	b = input().strip()
	if(n <1 or n > 100):
		raise SystemExit
	for i in range(len(b)):
		if((ord(b[i]) in range(65,91)) or (ord(b[i]) == 95)):
			continue
		else:
			raise SystemExit
	for i in range(n):
		if(b[i] in dict.keys()):
			dict[b[i]] =dict[b[i]]+  1
		else:
			dict[b[i]] = 1
	## Working till here
	flag = checkladybugs(n,b,dict)
	if(flag):
		print("YES")
	else:
		print("NO")
