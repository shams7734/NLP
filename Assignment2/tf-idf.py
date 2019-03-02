#2015KUCP1034
#Shams Ali
#Finding count vector and tf-idf
from __future__ import division
import nltk
import re
import math
mylist = []
mylist1 = []
mylist2 = []
mylistu = []
mylist1u = []
mylist2u = []
length1 = 0
length2 = 0
f = open("test1.txt", "r")
for line in f:
    mylist.extend(nltk.word_tokenize(line))
    mylist1.extend(nltk.word_tokenize(line))

for x in mylist1:
    if x is '.' or ' ' and len(x) == 1:
        mylist1.remove(x)
length1 = len(mylist1)
    
fp = open("test2.txt", "r")
for line in fp:
    mylist2.extend(nltk.word_tokenize(line))
    mylist.extend(nltk.word_tokenize(line))

for x in mylist2:
    if x is '.' or ' ' and len(x) == 1:
        mylist2.remove(x)
length2 = len(mylist2)

for x in mylist:
    if x is '.' or ' ' and len(x) == 1:
        mylist.remove(x)

for x in mylist:
    if x not in mylistu:
        mylistu.append(x)

for x in mylist1:
    if x not in mylist1u:
        mylist1u.append(x)

for x in mylist2:
    if x not in mylist2u and x not in mylist1u:
        mylist2u.append(x)

count1 = []
count2 = []
tf1 = []
tf2 = []
idf = []
tf_idf1 = []
tf_idf2 = []

k = 0
cal = 0
for x in mylistu:
    if x in mylist1 and x in mylist2:
        cal = math.log(2/2)
        idf.append(cal)
        k = k + 1
    else:
        cal = math.log(2/1)
        idf.append(cal)
        k = k + 1

i = 0
for x in mylistu: 
    if x in mylist1u:
        count1.append(mylist1.count(x))
        tf1.append((count1[i] / length1))
        tf_idf1.append((tf1[i]*idf[i]))
        print "Count vector of", x ,"in Document 1 is ", count1[i] ," TF is", tf1[i]," IDF is", idf[i] ,"and TF-IDF is", tf_idf1[i]
        i = i + 1

j = 0
for x in mylistu:
    if x in mylist2u:
        count2.append(mylist2.count(x))
        tf2.append((count2[j] / length2))
        tf_idf2.append((tf2[j]*idf[i]))
        print "Count vector of", x ,"in Document 2 is ", count2[j] ," TF is", tf2[j]," IDF is", idf[i] ,"and TF-IDF is", tf_idf2[j]
        j = j + 1
        i = i + 1
