#!/usr/local/bin/python
# -*- coding: gbk -*-
#============================================================
# TEST2.PY                     -- by Dr. ZhuoQing 2021-02-10
#
# Note:
#============================================================

from headm import *

#------------------------------------------------------------
f1 = lambda x: 2*(1-x**2)**0.5 - x*(pi-2*arcsin(x))

def e1func(gama):
    leftv = 0
    rightv = 1

    for i in range(100):
        midv = (leftv+rightv)/2
        e1 = f1(midv)
        e2 = pi * midv / gama

        if e1 == e2:
            return midv
        elif e1 < e2:
            rightv = midv
        else: leftv = midv

    return (leftv+rightv)/2

#------------------------------------------------------------
def e0func(e):
    t1 = arcsin(e)
    v1 = (t1-e*(1-e**2)**0.5)/pi
    v2 = 2*e**2*(pi/2-t1)/pi

    return sqrt(v1+v2)

#------------------------------------------------------------
def reqfunc(e):
    return e/(sqrt(2)/2-e)

#------------------------------------------------------------
r1 = linspace(0.01, 10, 100)
e1 = [e1func(g) for g in r1]
e0 = [e0func(e) for e in e1]
req = [reqfunc(e) for e in e0]
ratio = [v1/v2 for v1,v2 in zip(req, r1)]

printf(req)

plt.plot(r1, ratio)
plt.xlabel("R1")
plt.ylabel("Ratio")
plt.grid(True)
plt.tight_layout()
plt.show()

#------------------------------------------------------------
#        END OF FILE : TEST2.PY
#============================================================