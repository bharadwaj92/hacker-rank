import sys
import math
total_train = 0 ## Total rows in training
Train = []## Training matrix
dic = {}

def predict():
    total = 0
    test = []
    for line in sys.stdin:
        total = int(line)
        break
    for line in sys.stdin:
        line = line.replace('\n', '')
        l = []
        temp = line.split(' ')
        temp = [x for x in temp if x != '']
        for item in temp:
            if (item != 'is'
			and item != 'the'
			and item != 'an'
			and item != 'a'
			and item != 'its'
			and item != 'of'
			and item != 'in'
			and item != 'will'
			and item != 'has'
			and item != 'had'
			and item != 'and'
			and item != '|'
			and item != 'at'
			and item != 'am'
			and item != 'i'
			and item != 'of'
			and item != 'than'
			and item != 'can'
			and item != 'by'
			and item != 'vs'
			and item != 'or'
			and item != 'this'
			and item != 'with'
			and item != 'when'
			and item != 'over'
			and item != 'to'
			and item != 'by'
			and item != 'for'
			and item != 'there'
			and item != 'on'
			and item != 'off'
			and item != 'said'
			and item != 'could'):
                l.append(item)
        test.append(l)
    return test ,total
(test , total ) = predict()

def Train()
	df = open('train.txt')
	for line in df: 
		total = int(line)
		break
	for line in df: 
		Xtrain = []
		l = []
		line = line.replace('\n', '')
		temp = line.split(' ')
		#print(temp)
		temp = [x for x in temp if x != '']
		#print(temp[0])
		l.append(temp[0])
		item1 = temp[1: ]
		#print(item1)
		for item in item1: 
			if (item != 'is'
				and item != 'the'
				and item != 'an'
				and item != 'a'
				and item != 'its'
				and item != 'of'
				and item != 'in'
				and item != 'will'
				and item != 'has'
				and item != 'had'
				and item != 'and'
				and item != '|'
				and item != 'at'
				and item != 'am'
				and item != 'i'
				and item != 'of'
				and item != 'than'
				and item != 'can'
				and item != 'by'
				and item != 'vs'
				and item != 'or'
				and item != 'this'
				and item != 'with'
				and item != 'when'
				and item != 'over'
				and item != 'to'
				and item != 'by'
				and item != 'for'
				and item != 'there'
				and item != 'on'
				and item != 'off'
				and item != 'said'
				and item != 'could'
				and item != 'however'):
				Xtrain.append(item)
				#print(Xtrain)
		l.append(Xtrain)
			#print(l)
		Train.append(l)
	##print(Train[0][0])
	for i in range(len(Train)):
		y = Train[i][0]## Y value for each row
		x = Train[i][1] ##words list in each row
		if y in dic.keys():
			for j in range(0,len(x)):
				if x[j] in dic[y].keys():
					dic[y][x[j]] += 1
				else:
					dic[y][x[j]] = 1
		else:
			##print(type(Train[i][0]))
			dic[y] = {}
			for j in range(0,len(x)):
				if x[j] in dic[y].keys():
					dic[y][x[j]] += 1
				else:
					dic[y][x[j]] = 1
