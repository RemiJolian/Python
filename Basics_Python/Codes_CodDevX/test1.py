x = 35
print(x)
# --------
x = [1,2,3]
for item in x:
    print (item)

#----------
x = [9,2,8,4,1]
x.sort()
print (x)

#------
x = [5,3,6,3]
x.sort(reverse=True)
print (x)

#--------

x = 1,2,3
y = (3,4,5)
z = 9,
print (x,type(x))
print (y, type(y))
print (z, type(z))

#--------

x = (1,2,3)
# del x([1]) has error,it is emmutable
print (x)

#------

y = (1,[2,3],4)
del (y[1][0])
print (y)

#---------------------------------------
x = ['sara', 'homan','jina']
print (sorted(x,key=lambda k:k[1]))
