#2015KUCP1034
#Shams Ali
#Checking Similarity
from __future__ import division
import nltk
import re
mylist = ['']
f = open("training.txt", "r")
for line in f:
    mylist.extend(nltk.word_tokenize(line))
mylist1 = ['']
fp = open("testing.txt", "r")
for line in fp:
    mylist1.extend(nltk.word_tokenize(line))
count = 0
total = 0
for x in mylist1:
    if x in mylist:
        count = count + 1
total = len(mylist1)
percent = (count / total)*100
print("Similarity percentage is ")
print(percent)

    
