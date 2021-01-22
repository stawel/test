#!/usr/bin/python3

import random
import numpy as np

# Veritasium autronauts experiment but with a normal distribution
# https://www.youtube.com/watch?v=3LopI4YeC4I

debug = False
astronauts = 18300
n = 1000

#n = 2
#debug = True

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def find_intersection():
    #normal distribution, IQ scaled by 160 (skill should be betwieen [0,1])
    #https://en.wikipedia.org/wiki/Intelligence_quotient
    IQ, sigma = 100, 15
    skill = np.random.default_rng().normal(IQ, sigma, astronauts) / 160.
    #uniform distribution
    #skill = [ random.random() for i in range(astronauts) ]

    u1 = [ (i, skill[i] ,random.random()) for i in range(astronauts) ]
    u2 = [ (i, s * 0.95 + l * 0.05, s, l) for (i, s, l) in u1 ]

    ul, us = u2.copy(), u2.copy()

    ul.sort(reverse=True, key = lambda x : x[1])
    us.sort(reverse=True, key = lambda x : x[2])

    inter = [ i for (i, v, s, l) in intersection(ul[0:11], us[0:11])]
    if debug:
        print('luck:')
        for (i,v,s,l) in ul[0:11]:
            print('idx:',i,'sum:',v,'skill:',s,'luck:',l)

        print('skill:')
        for (i,v,s,l) in us[0:11]:
            print('idx:',i,'sum:',v,'skill:',s,'luck:',l)

        print('intersection')
        print(inter)
    return inter


r = 0
for i in range(n):
    r += len(find_intersection())

print('intersection avr:', r/n)

#normal distribution,  intersection avr: 8.323
#uniform distribution, intersection avr: 1.547
