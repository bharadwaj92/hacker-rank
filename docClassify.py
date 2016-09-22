import sys
import math
total_train = 0 ## Total rows in training
Train = []## Training matrix
total_test = 0
dic = {}
YprobbyClass = {}
YcountbyClass = {}
PrbXgivenY = {} # Y is key, and X has dict of K-V paris with P(X/Y)
PrbX = {}
CntXperW = {}
Classifylist = []
def create_test_data():
    test = []
    for line in sys.stdin:
        total_test = int(line)
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
    return test

def TrainM():
	df = open('trainingdata.txt')
	for line in df: 
		total_train = int(line)
		#print(total_train)
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
		l.append(Xtrain)
		Train.append(l)
	for i in range(len(Train)):
		y = Train[i][0]## Y value for each row
		x = Train[i][1] ##words list in each row
		if y in YcountbyClass.keys():
			YcountbyClass[y] += 1 
		else:
			YcountbyClass[y] = 1
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
	return (YcountbyClass,total_train , dic)
	
def cal_probability(YcountbyClass , total_train , dic):
	tot_words_training = 0 
	for key in YcountbyClass.keys():
		YprobbyClass[key] = YcountbyClass[key]/total_train
		YprobbyClass[key] = float("{0:.3f}".format(YprobbyClass[key]))
	for key1 in dic.keys():
		PrbXgivenY[key1] = {}
		for key2 in dic[key1].keys():
			 PrbXgivenY[key1][key2] = dic[key1][key2]/YcountbyClass[key1]
			 PrbXgivenY[key1][key2] = float("{0:.3f}".format(PrbXgivenY[key1][key2]))
	for key1 in dic.keys():
		for key2 in dic[key1].keys():
			if key2 in CntXperW.keys():
				CntXperW[key2] += dic[key1][key2]
				tot_words_training += dic[key1][key2] 
			else:
				CntXperW[key2] = dic[key1][key2]
				tot_words_training += dic[key1][key2] 
	for key in CntXperW.keys():
		PrbX[key] = CntXperW[key]/float(tot_words_training )
		PrbX[key] = float("{0:.3f}".format(PrbX[key]))
	#print(tot_words_training)
	return ( PrbXgivenY , PrbX ,YprobbyClass  )
			
def predict() :
    test = create_test_data()
    (YcountbyClass,total_train ,dic) = TrainM()
    (PrbXgivenY , PrbX ,YprobbyClass  ) = cal_probability(YcountbyClass, total_train, dic)
    for i in range(len(test)):
        PforeachY = {}
        for key in YprobbyClass.keys():
            Prtemp = 0 
            for j in range(len(test[i])):
                if test[i][j] in PrbXgivenY[key].keys():
                    #print(PrbXgivenY[key][test[i][j]])
                    Prtemp = Prtemp *( PrbXgivenY[key][test[i][j]])
                else:
                    continue
                Prtemp = (Prtemp * YprobbyClass[key])
            PforeachY[key] = Prtemp
        Classifylist.append(max(PforeachY ,  key = PforeachY.get))
    return(Classifylist )
print(preidct())
