import re
from collections import	namedtuple

dict3 = {}
f21 = open('count_blog.txt','r')
num = 0
for line in f21:
	num = num +1
	print num
	words = line.split('::')
 	p = words[0]
 	q = words[1]
	dict3[p] = q
f21.close()


dict={}
blog = namedtuple("blog", ["name", "number"])
f = open('tier1.txt', 'r')
n = 0
num = 0
for line in f:
 	words = line.split('::')
 	p = words[0].strip().decode('ascii', errors='ignore')
 	try:
 		if 15<= int(dict3[p].split('\n')[0])<= 25:
 			s = ''
 			q = words[1].strip().lower().decode('ascii', errors='ignore')
 			n = n +1
 			print n
			words1 = q.split('.')
 			w = 0
 			for sline in words1:
  				if w >6:
   					break
  				if len(sline.split())> 100:
   					continue
  				sline = sline + '.'
  				s = s + sline
  				w = w +1
 			blogs = dict.keys()
 			i = 1
 			for entry in blogs:
  				if entry.name==p:
   					i = i+1
 			if s == '':
 				s = q
 			dict[blog(p,i)] = s  # Input file is fed into dictionary dict
			
	except: 
		print 'error'
		num = num +1
f.close()


f5 = open('15-20containedblog.txt', "w")

for key in sorted(dict.keys()):
	f5.write(str(key)+ '::')
	f5.write(str(dict[key]))
	f5.write('\n')
f5.close()

dicts = {}
f1 = open('15-20containedblog.txt','r')
for line in f1:
	words = line.split('::')
 	dicts[words[0]]=words[1]
f1.close()


dicts1 = {}
f2 = open('mylist15_20.csv')
for line in f2:
	words = line.split('\n')
 	dicts1[words[0]]=dicts[words[0]]
f2.close()

f52 = open('15-20containedblog1.txt', "w")
for key in sorted(dicts1.keys()):
	f52.write(str(key)+ '::')
	f52.write(str(dicts1[key]))
f52.close()


f51 = open('15-20containedblog.txt_tier1.txt', 'w')
f53 = open('15-20containedblog1.txt', "r")
i = 1
for line in f53:
	word = line.split('::')
	auth1 = re.search(r'name=u(.*), n' , word[0])
	f51.write(str(auth1.group(1))+ '::')
	f51.write(str(word[1]))   
	i = i +1
print i
	


f53.close()
