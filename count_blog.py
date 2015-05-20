dict3 = {}
f21 = open('tier1.txt','r')
num = 0
for line in f21:
	num = num +1
	print num
	words = line.split('::')
 	p = words[0].strip().decode('ascii', errors='ignore')
	if p in dict3.keys():
		dict3[p] = dict3[p] +1
	else:
		dict3[p] = 1
f21.close()

f = 0
for p in dict3.keys():
	 f = f + dict3[p]
print f

for (author, Blog) in dict3.iteritems():
    with open('count_blog.txt', "a") as f5:
        f5.write(str(author)+ '::')
        f5.write(str(Blog))   
        f5.write('\n')
