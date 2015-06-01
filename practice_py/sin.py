#!/usr/bin/env python
#coding:utf-8

import pylab
import random
import math
import matplotlib.pyplot as plt

frameN = pylab.arange(1, 400)
phi = random.uniform(0, 2*math.pi)
i = 2*math.pi*(frameN/400)
f = (pylab.sin(i+phi)+pylab.sin(2*i+phi)+pylab.sin(4*i+phi))/3

plt.plot(f)
plt.ylim([-1.0, 1.0])

plt.show()
