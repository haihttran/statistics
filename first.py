# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:19:13 2017

@author: tranh
"""
import math
import survey
import thinkstats
table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies', len(table.records))
count = 0
first = 0
other = 0
firstchild = []
otherchild = []
first_prglength = 0
other_prglength = 0
#Loop through the dataset and look for first child
for r in table.records:
    if r.outcome == 1:
        count = count + 1
        #Count for the number of first child and sum total first child pregnancy length
        if r.birthord == 1:
            first = first + 1
            firstchild.append(r.prglength)
            first_prglength = first_prglength + r.prglength
        #Count for the number of other child and sum total other child pregnancy length
        else:
            other = other + 1
            otherchild.append(r.prglength)
            other_prglength = other_prglength + r.prglength
print('Number of live births:', count)
print('Number of first children:', first)
print('Number of other children:', other)
print('Average first children pregnancy length:', first_prglength/first)
print('Average other children pregnancy length:', other_prglength/other)
#Standard deviation of fisrt and other children
print('Standard deviation of gestation of the firstchild: ', math.sqrt(thinkstats.Var(firstchild)))
print('Standard deviation of gestation of the otherchild: ', math.sqrt(thinkstats.Var(otherchild)))