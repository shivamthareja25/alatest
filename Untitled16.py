#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number= input("Enter a number : ")
listA= ['1','268','46','4620','468','4632','4673','46732']
costA=[0.9,5.1,0.17,0.0,0.15,0.15,0.9,1.1]
listB=['1','44','46','467','48']
costB=[0.92,0.5,0.2,1.0,1.2]
n=len(listA)
m=len(listB)
dictA= dict(zip(listA,costA)) 
dictB= dict(zip(listB,costB))
newnumb= ""
newvar= ""
operatorA = []
operatorB = []
if ('+' in number) or ('-' in number) or (' ' in number):
    for s in number:
        if (s != "+") and (s != "-") and (s != " "):
            newnumb = newnumb+s
else:
    newnumb=number
    
for i in range(n):
    if listA[i] in newnumb:
        for f in range(len(listA[i])):
            newvar= newvar + newnumb[f]
        if newvar == listA[i]:
            operatorA.append(newvar)
            newvar = ''


for i in range(m):
    if listB[i] in newnumb:
        for f in range(len(listB[i])):
            newvar= newvar + newnumb[f]
        if newvar == listB[i]:
            operatorB.append(newvar)
            newvar = ''


operatorA = [int(i) for i in operatorA]
operatorB = [int(i) for i in operatorB] 

for b in operatorB:
    operatorA.append(b)

operatorA.sort(reverse=True)


operators=[]

try:
    length = len(str(operatorA[0]))

    operators=[a for a in operatorA if len(str(a))==length]





    if len(operators) > 1 :
            if dictB[str(operators[0])] > dictA[str(operators[0])]:
                print(f"You can use both the operators for calling but operator A is cheaper at ${dictA[str(operators[0])]}/ minute  than operator B which will cost ${dictB[str(operators[0])]}/ minute ")
            else :
                print(f"You can use both the operators for calling but operator B is cheaper at ${dictB[str(operators[0])]}/ minute  than operator A which will cost ${dictA[str(operators[0])]}/ minute ")
    elif str(operators[0]) in dictA:
         print(f'You can use only operator A for calling ,you will have to pay ${dictA[str(operators[0])]}/ minute')
    else:
         print(f'You can use only operator B for calling ,you will have to pay ${dictB[str(operators[0])]}/ minute')
    
except IndexError : 
    print(" No such prefix exists")


