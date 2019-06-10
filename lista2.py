# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:44:51 2019

@author: Caio
"""

def media2(a,b):
    return (a+b)/2

def media4(a,b,c,d):
    return (media2(a,b)+media2(c,d))/2

def ex1b(preco,dinheiro):
    return dinheiro//preco,dinheiro%preco

from math import sqrt,sin,cos,pi

def ex2a(a,b):
    return sqrt(a**2+b**2)

def ex2b(x0,y0,x1,y1):
    return sqrt((x1-x0)**2+(y1-y0)**2)    

def ex2c(a,b):
    return a+b+ex2a(a,b)

def ex2d(theta):
    return sin(theta)**2+cos(theta)**2

def ex3(r):
    return 2*pi*r

def ex4(r,distancia):
    return distancia//ex3(r)

def delta(a,b,c):
    return b**2-4*a*c

def raizes(a,b,c):
    return (-b+sqrt(delta(a,b,c)))/(2*a),(-b-sqrt(delta(a,b,c)))/(2*a)

def setorcircular(raio,angulo=360):
    return angulo*pi*raio**2/360

def ex7a(A1,An,r):
    return (An-A1)/r + 1

def ex7b(A1,An,r):
    return (A1+An)*ex7a(A1,An,r)/2

def ex8(A,B,C):
    return ((A/2) + (B/3) + (C/5))//3