import sys
import numpy as np
from collections import Counter

def calc_freq(original_list, item):
    counter = 0
    checker = True
    
    for a in original_list:
        c = Counter(a)
        for b in range(0,len(item)):
            if c[item[b]] != 1:
                checker = False
        if checker == True:
            counter = counter+1
        checker = True
    result = counter
    return result
        
file = open(sys.argv[1], 'r')
outputfile = sys.argv[2]
minsup = float(sys.argv[3])

buff = []
buff = file.readlines()
file.close()

list_temp = []
original_list = []
counter = 0
for i in buff:
    splitted = i.split(', ')
    for j in splitted:
        if j.find('\n') != -1:
            j_temp = j[1:-2]
        else:
            j_temp = j[1:-1]
        list_temp.append(j_temp)

for k in list_temp:
    original_list.append(k.split(' '))
 
 
candidate_1 = list(sorted(set(x for l in original_list for x in l)))
list3 = []
list3.append('2')
list3.append('3')
list3.append('4')

minsup = minsup*len(original_list)
candidate_k = []
freq_items = []
for i in candidate_1:
    freq = calc_freq(original_list, i)
    if freq >= minsup:
        freq_items.append(list(i))
        freq_items.append(freq)
        candidate_k.append(list(i))

while len(candidate_k)!= 0:
    candidate_nonpruned = []

    for i in range(0,len(candidate_k)):
        for j in range(i+1,len(candidate_k)):
            if candidate_k[i][1:len(candidate_k[i])] == candidate_k[j][0:len(candidate_k[j])-1]:
                list_temp2 = []
                for k in candidate_k[i]:
                    list_temp2.append(k)
                list_temp2.append(candidate_k[j][len(candidate_k[j])-1])
                candidate_nonpruned.append(list_temp2)
    candidate_temp = []
    for i in candidate_nonpruned:
        if calc_freq(original_list, i) >= minsup:
            candidate_temp.append(i)
    candidate_pruned = []
    
    for i in candidate_temp:
        subsets = []
        for j in i:
            i_temp = []
            for k in i:
                i_temp.append(k)
            i_temp.remove(j)
            subsets.append(i_temp)
        checker2 = True
        for k in subsets:
            if k not in candidate_k:
                checker2 = False
        if checker2 == True:
            candidate_pruned.append(i)
    if len(candidate_pruned) != 0:
        for c in candidate_pruned:
            freq_items.append(c)
            freq = calc_freq(original_list, c)
            freq_items.append(freq)
    candidate_k = candidate_pruned

file2 = open(outputfile,'w')
for i in range(0,len(freq_items),2):
    st = "pattern: "+str(freq_items[i])+" support value: "+str(freq_items[i+1])+"\n"
    file2.write(st)
file2.close()       
                



















