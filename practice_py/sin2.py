#!/usr/bin/env python
#coding:utf-8

import pylab
import random
import math


def distance_check():

    f0 = 0
    distance = 0
    distance_f = 0
    frameN = pylab.arange(1, 600)
    phi = random.uniform(0, 2*math.pi)

    for n in frameN:
        i = 2*math.pi*(n/600)
        f = (pylab.sin(i+phi)+pylab.sin(2*i+phi)+pylab.sin(4*i+phi))/3
        distance_f = math.fabs(f - f0)
        distance += distance_f
        f0 = f

    print(distance)

for e in range(1, 11):
    distance_check()