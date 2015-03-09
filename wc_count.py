# This script is generated to count and print the occurences of specific word in
# a given text file
# Author: Ling Qi/lq38@cornell.edu

# Processing input file into list of words
import re
file = open('test.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
words.sort()

# function to create a list of words with unique occurences
def uniFind(seq): 
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked
uni = uniFind(words)

# Write to output file
output = open('wc_output.txt','w')
for i in range(0, len(uni)):
   output.write('%s\t' % (uni[i]),)
   output.write('%s\n' % (words.count(uni[i])))
output.close()
 
