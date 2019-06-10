# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:11:45 2019

@author: Caio
"""

def ex1(a,b):
    return a*b

def ex2(r1,r2):
    return 3.14*(r1**2-r2**2)

def ex3(a,b):
    return a/b,a%b

def ex4(a,b,c):
    x = -b/(2*a)
    y = a*x**2+b*x+c
    return x,y

def ex5(p):
    return 0.1*p

def ex6(a,b):
    return (a+b)/2

def ex7(a,pa,b,pb):
    return (a*pa+b*pb)/(pa+pb)

def ex8(vc,lr,vb):
    return vc*lr/vb

def ex9(saldo,meses,taxa):
    return saldo(1+meses*taxa)

def ex10(q,n):
    soma =  1/(1-q)
    termo_n = (q**n-1)/(q-1)
    return soma,termo_n,soma-termo_n

def ex11(hi,mi,si,hf,mf,sf):
    tempo_total = (hf*60**2+mf*60+sf)-(hi*60**2+mi*60+si)
    return tempo_total//(60**2),tempo_total//60 - (tempo_total//(60**2))*60,tempo_total % 60

def ex12(valor,pessoas):
    return (valor*0.1),(valor*0.1)/pessoas

def ex13(aresta):
    return 6*aresta**2