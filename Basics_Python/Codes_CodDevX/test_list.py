under10 = [x for x in range(10)]
print ('under10 is :' , str(under10))

square = [x**2 for x in range(10)]
print ('square is :', square)

# get odd number:
oddNum = [x for x in range(10) if x%2 == 1]
print ('oddNum is :', oddNum) #or:print ('oddNum is :', str(oddNum))
multiple10 = [x*10 for x in range(10)]
print ('multiple10 is :', multiple10)
#-----------------------------------
#get num:
s = 'I love 2 go to st4re 7 times a we3k'
nums = [x for x in s if x.isnumeric()]
print('nusm is ',nums)
print ('++++++++++++++')
#print('nums ', + '', .join(nums)) ??? why error eccure

#------------------------------------------------------------
names = ['cosmo','baloon','cloud']
idx = [k for k, v in enumerate(names) if v == 'baloon']
print (idx)
print ('index :', str(idx[0]))

#------------------------------------------------------------
letters = [x for x in 'ABCDEF']
#random.shuffle(letters)
lett = [a for a in letters if a !='C']
print (letters, lett)
print ('++++++++++++++')
print ('++++++++++++++')

#-------------------------------------------
a = [[1,2],[3,4]]
newList = [x for b in a for x in b]
print (newList) 

print ('------------------aaa--------------------')
#stack using list:
myStack = list()
myStack.append(4)
myStack.append(7)
myStack.append(12)
myStack.append(19)

print (myStack)
print (myStack.pop())
print (myStack.pop())
print (myStack)


