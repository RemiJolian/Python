x = {'baran':19, 'sara':18,'darya':17}
print (x)
x = dict([('baran',19),('sara',18),('darya',17)])
print (x)
x = dict(baran=19,sara=18,barya=17)
print (x)

x['mehrdad'] = 19.5
print (x)

print (len(x))

del (x['sara'])
print (x)

x.clear()
print (x)

del (x)
#------------------------------------------------

print ('-------------------------Baran------------------------')
y = {'baran':18.5, 'sara':17,'darya':15.75}
print (y.keys())
print (y.values())
print (y.items())
print ('mahor' in y)
print ('18.5' in y.values())
print (18.5 in y.values())

print("------------------bb-----------------")
for i in y:
    print(i) #it only print keys

for key in y:
    print (key,y[key])

# also we can write:
 # for k,v in y.items():
  #  print (k,v)??


