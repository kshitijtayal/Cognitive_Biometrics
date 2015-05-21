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


file = open('tier1.txt','r')
file1 = open('samplesen.txt','w')
for line in file:
    words = line.split('::')
    p = words[0].strip().decode('ascii', errors='ignore')
    try :
        if int(dict3[p].split('\n')[0]) >100:
            q = words[1].strip().lower().decode('ascii', errors='ignore')
            m = q.split('.')
            for splitline in m:
                if len(splitline.split()) > 6:
                    q =  p + '::' + splitline
                    file1.write(q)
                    file1.write('\n')
                    print q
    except:                      # capture error while loading file
        print 'error'
