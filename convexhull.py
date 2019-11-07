# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:58:21 2019

@author: amind
"""
from utils import create_points
from utils import determinant
from utils import distance_from_point_to_line
from utils import point_in_polygon
from utils import polar_angle
from utils import polar_quicksort
from utils import angle
from utils import distance
from numpy import pi
import matplotlib.pyplot as plt
import numpy as np




def jarviss(points):
    # initialiser le pivot p
    y=[y[1] for y in points]
    x=[x[0] for x in points]
    indices = [i for i, n in enumerate(y) if n == min(y)]
    min_x=999
    for k in indices:
        if x[k]<min_x:
            pivot=points[k]
            
    #placer le pivot en derniere position
    L=[i for i in points]
    L[len(L)-1],L[points.index(pivot)] = L[points.index(pivot)],L[len(L)-1]    
    #initialiser l'enveloppe
    hull=[pivot]
    while True:
        q=L[0]
        m=0
        for r in range(1,len(L)):
            if determinant(pivot,q,L[r])>0:
                q=L[r]
                m=r
        if q==hull[0]:
            break
        else:
            hull.append(q)
            pivot=q
            del L[m]

    return hull
    


def floyd(points,min,max):
    upper_points=[point for point in points if determinant(min,max,point)>0]
    farthest_point=[-1,-1]
    dist_max=0
    for point in upper_points:
        if point not in [min,max]:
            d=distance_from_point_to_line(point, [min,max])
            if d>dist_max:
                dist_max=d
                farthest_point=point
    if farthest_point==[-1,-1]:
        return [max]
    
    hull=floyd(upper_points,min,farthest_point)
    hull+=floyd(upper_points,farthest_point,max)
    return hull
    
def hull_floyd(points):
    hull=[]
    x=[x[0] for x in points]
    p=points[x.index(min(x))]
    q=points[x.index(max(x))]

    #inspecter le haut de la droite
    hull=floyd(points,p,q,)
    #inspecter le bas de la droite
    hull+=floyd(points,q,p)
    return hull



def graham(points):

    # initialiser le pivot p
    y=[y[1] for y in points]
    x=[x[0] for x in points]
    indices = [i for i, n in enumerate(y) if n == min(y)]
    min_x=999
    for k in indices:
        if x[k]<min_x:
            pivot=points[k]
            min_x = x[k]
          
    #placer le pivot en derniere position
    L=[i for i in points]
    L[len(L)-1],L[points.index(pivot)] = L[points.index(pivot)],L[len(L)-1]
    
    #trier la liste suivant les angles faits avec le pivot
    Lnew = polar_quicksort(L,pivot)
    for i in range(0,len(Lnew)-2):
        if i+1<len(Lnew):
            if polar_angle(pivot, Lnew[i]) == polar_angle(pivot,Lnew[i+1]):
                if distance(pivot, Lnew[i]) > distance(pivot, Lnew[i+1]):
                    del Lnew[i+1]
                else:
                    del Lnew[i]          
    #initialiser l'enveloppe 
    hull=list(Lnew)
    n=len(Lnew)
    hull = []
    hull.append(Lnew[0])
    hull.append(Lnew[1])
    hull.append(Lnew[2])
    for i in range(2,n):
        while (True):
            d = determinant(Lnew[i],hull[-1], hull[-2])
            if d < 0: # if it makes left turn
                break
            else: # if it makes non left turn
                hull.pop()
            if len(hull)<3:
                break
        hull.append(Lnew[i])
    return hull