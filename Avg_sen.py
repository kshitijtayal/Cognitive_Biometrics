import re
from collections import	namedtuple

sent = []
f = open('tier1.txt', 'r')
n = 0
num = 0
for line in f:
 	words = line.split('::')
 	q = words[1].strip().lower().decode('ascii', errors='ignore')
 	n = n +1
 	print n
	words1 = q.split('.')
	sent.append(len(words1))


print (sum(sent)/(float(len(sent))))

