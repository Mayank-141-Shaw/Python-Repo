# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:19:40 2020

@author: MAYANK SHAW
"""

import matplotlib.pyplot as plt
import random as rd
import numpy as np
import copy
import math as mt

cities = []
for x in range(15):
    cities.append(rd.sample(range(100), 2))             #randomly chooses a set of size 2 from list [0 to 100] given by range()
    
#this randomizes our city cordinatees    
#this gives us 15 cities
tour = rd.sample(range(15), 15);

#this starts our tour with a random tour connectng cities
for temp in np.logspace(0, 5, num=100000)[::-1]:
    [i,j] = sorted(rd.sample(range(15), 2));
    newTour = tour[:i] + tour[j:j+1] + tour[i+1:j] + tour[i:i+1] + tour[j+1:];
    if mt.exp((sum([mt.sqrt(sum([(cities[tour[(k+1)%15]][d])**2 for d in [0,1]])) for k in [j,j-1,i,i-1]]) - sum([mt.sqrt(sum([(cities[newTour[(k+1)%15]][d] - cities[newTour[k%15]][d])**2 for d in [0,1]])) for k in [j,j-1,i,i-1]])) / temp)>rd.random():
        tour = copy.copy(newTour);

plt.plot([cities[tour[i%15]][0] for i in range(16)], [cities[tour[i%15]][1] for i in range(16)], 'xb-');
plt.show()
