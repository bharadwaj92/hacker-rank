## Sherlock and probability https://www.hackerrank.com/challenges/sherlock-and-probability
from fractions import Fraction
from sys import stdin
import math 
def find_prob(arr,l,k):
    num = 0
    den = int(math.pow(l,2))
    for i in range(0,l):
        if(arr[i] == False):
            continue
        for j in range(0,l):
            if( abs(j-i) > k):
                continue
            elif((arr[i] == arr[j] ==True) and abs(j-i) <= k):
                num +=1
    return num , den
            
n = int(stdin.readline().strip())
if(n > math.pow(10,5) or n< 1):
    raise SystemExit
sum = 0
for i in range(n):
    temp1 = []
    arr = []
    temp = stdin.readline().strip().split(" ")
    temp1 = stdin.readline().strip()
    for i in range(len(temp1)):
        arr.append(bool(int(temp1[i])))
    l =int(temp[0])
    sum += l
    k = int(temp[1])
    if(k < 1 or k > l):
        raise SystemExit
    if(len(arr) > math.pow(10,5) or n <1):
        raise SystemExit
    (num,den) = find_prob(arr,l,k)
    if(l == k or l == k-1):
        print(str(1)+"/"+str(1))
    if(num == 0):
        print (str(0)+"/"+str(1))
    else:
        x=Fraction(int(num),int(den))
        res = str(x.numerator)+"/"+str(x.denominator)
        print(res)
if(sum > math.pow(10,5) or sum <1 ):
    raise SystemExit
