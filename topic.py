from numpy import ndarray
import numpy
a = numpy.empty((14884,50), float)


f1 = open('/Users/kshitijtayal/Documents/mallet/x.txt','r')
row = 0
for line in f1:
	line1 = line.split('\t')
	for i in range(2,101,2):
		p = i +1
		print i ,p
		a[row,int(line1[i])] = float(line1[p])
	row = row +1
f1.close()

te = open('outputfile.txt','w')
for row in a:
	te.write(','.join('%f' % i for i in row)+'\n')
te.close()
