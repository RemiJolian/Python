

#length

x = 'Baran'

print (len(x))

​

y = ['Sara','Darya']

print (len(y))

​

z = ('babr','jojo','kalagh')

print (len(z))

    

5
2
3

#max and min 

x = 'baran'

print (min(x))

​

y = ['cow','jo','p','hora']

print (min(y))

​

z = ('43','876')

print (min(z))

a
cow
43

x = 'hora'

print (max(x))

​

y = ['sohi','jadi','bo']

print (max(y))

​

z= ('jadi','emad','peterson')

print (max(z))

r
sohi
peterson

x = [2,1,'bar']

#prin (sum(x))------->error

​

y = [2,4,5,6,9]

print (sum(y))

print (sum(y[1:]))

print (sum(y[-2:]))

print('--------')

z = (2,4,5)

print (sum(z))

26
24
15
--------
11

#sorting by alphabet

x = 'horse'

print (sorted(x))

​

y = ['hapoo','piter','jojo']

print (sorted(y))

​

z = ('kevin','hapson','dogi')

print (sorted(z))

['e', 'h', 'o', 'r', 's']
['hapoo', 'jojo', 'piter']
['dogi', 'hapson', 'kevin']

x = 'hapoo'

print (x.count('o'))

print (x.count('j'))

print ('--------------')

​

y = ['jojo','popo','lolo']

print (y.count('jojo'))

print ('--------------')

​

z = ('hi','shenya','jwana','shenya')

print (z.count('shenya'))

2
0
--------
1
--------------
2------

#unpacking n item in a sequence

x = ('cat','car','tree')

a,b,c = x

print (a,b,c)

cat car tree

