from __future__ import division
import numpy

sdata = []
i =1
with open('myfile15_20.csv') as s:   # name of the file
    for sline in s:
    	sline = sline.strip()
        y = 0
        for x in sline.split(","):
        	y = y + int(x)
        svals = [int(x)/y for x in sline.split(",")]
        sdata.append(svals)
        i = i +1
        print i
sdata1 = numpy.array(sdata)

numpy.savetxt('normalized.csv', sdata1, delimiter=',')   # X is an array #output
