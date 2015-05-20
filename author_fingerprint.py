import numpy
from numpy import genfromtxt
import re
my_data = genfromtxt('finalcombined1.csv', delimiter=',')
print my_data.shape

i = 0
z = 0
kn = 0
sdata = []
file = open('mylist5.csv','r')
for line in file:
        if i == 0:
            x =  line.split('\n')[0]
            auth1 = re.search(r'name=u(.*), n' , x)
            y = auth1.group(1)
            i = i + 1
        else:
            x =  line.split('\n')[0]
            auth1 = re.search(r'name=u(.*), n' , x)
            if auth1.group(1) == y:
                i = i + 1
            else:
                y = auth1.group(1)
                p = my_data[z:i,:]
                avg = numpy.mean(p,axis = 0)
    
                z = i
                i = i +1
                sdata.append(avg)  
sdata1 = numpy.array(sdata)
print sdata1.shape
numpy.savetxt("author.csv",sdata1, delimiter=',')

