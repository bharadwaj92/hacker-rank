# Enter your code here. Read input from STDIN. Print output to STDOUT
# I believe the 3rd test case of 2nd input's expected answer is incorrect.
# (AB)C/RS => C(BA)/S => CBA. But the expected answer is given as C(BA) which is incorrect according to my belief. 
# Custom test cases : 
#1) (AB)C(D(EF))/SS => ABC(DEF) 2)(AB)C(D(EF))/RS => (FED)CBA
#2) (AB)C(D(EF)Y(X))/S => ABC(DEFYX) 2) (AB)C(D(EF)Y(X))/RR => (AB)C(D(EF)Y(X))
#  (AB)C(D(EF)Y(X))/RS =>(XYFED)CBA (AB)C(D(EF)Y(X))/SS => ABC(DEFYX)
import re
from sys import stdin
from sys import stdin
#array of the input read from STDIN
input = []
#Function for simplify operation
def simplify_expr(exp):
    res = ""
    #Splitting by open paran 
    temp = exp.split("(")
    for i in temp:
        if(i == ""):
            continue #If the element is null , just continue
        else:
            count = 0
            item = ""
            for j in i:
                if(j == ')'):
                    count+= 1 # Counting closing pran in element
            if(count == 0):
                continue # If no closing pran, just let it be
            elif(count == 1):
                itemindex = temp.index(i)
                for p in i:
                    if(p==')'):
                        continue #If the element has only single closing pran,remove it& modify temp
                    else:
                        item = item + p
                temp[itemindex] =temp[itemindex-1] +item # Assigning modified list element to temp.
                temp[itemindex-1]=""
            elif(count >1):# If closing pran > 1
                ir = "" # Build a new array item by simplifying the expression
                cclosing = 0 #track the first closing brace to merge 
                itemindex = temp.index(i)
                for p in i:
                    if(p != ")"):
                        ir = ir + p
                    else:
                        cclosing += 1
                        if(cclosing == 1):
                            continue
                        else:
                            ir = ir + p # Revmoing one first paran of nested paran
                temp[itemindex] = temp[itemindex-1] + ir # Combining before and current element 
                temp[itemindex-1] = ""
                appendcount = count -1
                updateindex = itemindex -2				
                while(appendcount > 0):# adding open paran to count -1 predecessor items 
                    temp[updateindex] = temp[updateindex]+str("(") 
                    appendcount -= 1
                    updateindex -= 1					
                    
    for g in temp:
        if(i == ""):
            continue
        else:
            res = res + g # Generating resultant string
    return res
# Function for reverse operation   
def reverse_expr(exp):
    res =""	
    for i in reversed(exp):# Checking reversed expression
        if(i == " "): 
            continue
        if(i == ')'):# If open paran, replace by closed paran and vice versa
            res = res+str('(')
        elif(i=='('):
            res = res+str(')')
        else:
            res = res+i
    return res
# Function to perform the opertaions in input
def perform_operations(x):
    result = []
    for i in range(len(x)):
        if(len(x[i][0]) == 1):
            # If there is only one operand in the expression, return itself irrespective of opertion
            result.append(x[i][0])
        elif(len(list(set(x[i][1]))) ==1 and list(set(x[i][1])) == list('R') and len(x[i][1]) %2 ==0):
            # If there are even number of R operations, then the result will be same as initial exp
            result.append(x[i][0])
        elif((x[i][1]) == ""):
            #If the operation list is empty, return the expression itself.
            result.append(x[i][0])
        else:
            scount = 0
            for z in x[i][1]:
                if(z == " "):
                    continue
                elif(z == 'S'):
                    scount += 1 # Tracking S count to perform only 1 S operation on expression
                    if(scount ==1):
                        x[i][0] = simplify_expr(x[i][0])
                    else:
                        continue
                elif(z == 'R'):
                    x[i][0] = reverse_expr(x[i][0])
            result.append(x[i][0])
    return result

while(1):
    temp = stdin.readline()
    if(temp == ""):
        break 
    else:
        #splitting input into expression part and operation par.
        input.append(temp.strip().split("/"))
#print(input)
res =perform_operations(input)
for x in range(len(res)):
    print(res[x])
