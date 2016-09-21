##calculation of Pearson correlation coefficient without scipy
##sample data set :
##Physics Scores  15  12  8   8   7   7   7   6   5   3
##History Scores  10  25  17  11  13  17  20  13  9   15

import sys
import math
PS = []
HS = []
def inputtaking():
    for line in sys.stdin:
        line = line.replace('\n', '')
        temp = line.split(' ')
        temp = [x for x in temp if x != '']
        temp = [x for x in temp if x != '\n']
        if(temp[0] == 'Physics'):
            #print(temp[3:6])
            PS.extend(temp[2:len(temp)])
        else:
            HS.extend(temp[2:])
    return(PS, HS)
(PS, HS) = inputtaking()
PS = list(map(int, PS))
HS = list(map(int, HS))
PSsum = sum(PS)
HSsum = sum(HS)
PSHS =0
for i in range(len(PS)):
    PSHS += PS[i]*HS[i]
NU = (PSHS - (PSsum*HSsum)/len(PS)) 
Ps2sum = 0
Hs2sum = 0
for i in range(len(PS)):
    Ps2sum += pow(PS[i],2)
    Hs2sum += pow(HS[i],2)
DN = math.sqrt((Ps2sum - Ps2sum/float(len(PS)))*(Hs2sum - Hs2sum/float(len(HS))))
Prcoeff = NU/float(DN)
print(Prcoeff)
