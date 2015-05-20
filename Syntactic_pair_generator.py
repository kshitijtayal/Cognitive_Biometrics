import os
import re
import sys
import collections
import numpy as np
from nltk.tree import Tree
from nltk.parse import stanford
import nltk
from collections import	namedtuple
from itertools import islice
from multiprocessing import Process, Manager
from collections import OrderedDict
import multiprocessing


os.environ['JAVAHOME'] = 'C:/Program Files/Java/jdk1.8.0_25/bin'
os.environ['STANFORD_PARSER'] = '/home/kshitij/Desktop/jars'
os.environ['STANFORD_MODELS'] = '/home/kshitij/Desktop/jars'

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
f21.close()  # Input File containing number of blogs per author

dict={}
blog = namedtuple("blog", ["name", "number"])
f = open('tier1.txt', 'r')
n = 0
num = 0
for line in f:
 	words = line.split('::')
 	p = words[0].strip().decode('ascii', errors='ignore')
 	try:
 		if 25<= int(dict3[p].split('\n')[0])<= 30:  # checks number of blogs
 			s = ''
 			q = words[1].strip().lower().decode('ascii', errors='ignore')
 			n = n +1
 			print n
			words1 = q.split('.')
 			w = 0
 			for sline in words1:
  				if w >6:     # Number of lines :7
   					break
  				if len(sline.split())> 100:  # A Sentence should not exceed 100 words 
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
			
	except:                      # capture error while loading file
		print 'error'
		num = num +1
f.close()



def get_file():
 
 manager = Manager()
 features = manager.dict()   # synchronize dictionary for multiprocessing
 
 nprocs = []   # saves the process
 
 for item in chunks(dict, 363):    #Specify number of tuples in single thread
  	n = multiprocessing.Process(target=get_features, args=(item,features ))   # multiprocessing 
  	nprocs.append(n)
  	n.start()
 
 for i in nprocs:   
 	 i.join()        # waiting for all the process to finish
 
 dicts = OrderedDict()  # Dictionary whose order is fixed
 
 for key in sorted(features.keys()): 
   dicts[key]= get_count(features[key])   # counts syntactic pairs
   
    
                           

 f1 = open('mylist25_30.csv','w') 
 for item in dicts.keys():
   f1.write('%s\n' % str(item))   # outputs the author name order
 f1.close()
 
 keys = set(k for d in dicts.values() for k in d)
 f = {k: [d.get(k, 0) for d in dicts.values()] for k in keys}     #arranges in matrix
 
 for (x,y) in f.iteritems():
  with open('file25_30.txt', "a") as f11:
    f11.write(str(x)+'::')
    f11.write(str(y))
    f11.write('\n')
 matrix(f)
    
 
 
def chunks(data, SIZE=1000000):  
    it = iter(data)
    for i in xrange(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}

def get_features(dict,features ):  
 	print 'inside get_features'   
 	parser = stanford.StanfordParser(model_path="/home/kshitij/Desktop/Project/englishPCFG.ser.gz")
 	k = 0
 	for key in dict.keys():
 	  	sentences = parser.raw_parse((dict[key].decode('ascii ',errors='ignore')))  # Tree generation
 	  	n = list(tails([list(i)[0] for i in sentences]))    #  syntactic pair generation
 	  	features[key] = n
 	  	k = k + 1
 	  	print k
 
def get_count(doc):
	pair1 = collections.Counter(doc)
	return pair1
 
def matrix(pairs):    # print matrix
 print 'inside_matrix'
 f2 = open('myfile25_30.csv','w')
 header = ''
 for key in pairs.keys():
    if header == '':
        header = '%s' %(str(key))
    else:
        header = '%s, %s' % (header, str(key))
 f2.write('%s\n' % header)

 for i in range(len(dict.keys())):
    line = ''
    for key in pairs.keys():
        if line == '':
            line = '%s' %pairs[key][i]
        else:
            line = '%s, %s' % (line, pairs[key][i])
    f2.write('%s\n' % line)
 f2.close()

def tails(items, path=()):  # return syntactic pairs 
   for child in items:
        if type(child) is nltk.Tree:
            if child.label() in {".", ",",":","``","''"}:  # ignore syntactic pairs which ends in punctuation
                continue
            for result in tails(child, path + (child.label(),)):
                yield result
        else:
            yield path [-2:]  

def main():
 	get_file()
 
if __name__ == '__main__':
 main()
