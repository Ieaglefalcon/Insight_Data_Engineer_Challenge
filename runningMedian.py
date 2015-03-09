# This script is to compute a running median of the word count of a given text
# Author: Ling Qi/lq38@cornell.edu

# Parsing text...
import math

with open('test.txt') as f:
    lines = f.readlines()
    
# Iterating through all items...
length = []
median = []
for item in lines:
        lineLen = len(item.split())
        length.append(lineLen)
        length.sort()
        
	# compute median...
        if len(length) % 2 != 0:
                id = math.ceil(len(length)/2) - 1
                newMedian = length[id]
                median.append(newMedian)
        else:
                id1 = math.ceil(len(length)/2 - 1)
                id2 = math.ceil(len(length)/2)
                newMedian = (length[id1] + length[id2])/2
                median.append(newMedian)

# Write to output file
output = open('rm_output.txt','w')
for i in range(0, len(median)):
   output.write('%s\t' % (median[i]))
output.close()
