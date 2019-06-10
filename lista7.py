# -*- coding: utf-8 -*-
"""
Lista 7 de Comp 1
"""
def ex1():
    A = 80000
    B = 200000
    contador = 0
    while A<B:
        A*=1.03
        B*=1.015
        contador+=1
    return contador

def ex2(A,B,taxA,taxB):
    contador = 0
    while A<B:
        A+=A*taxA/100
        B+=B*taxB/100
        contador+=1
    return contador

def ex3():
    from random import randint
    contador = 0
    while True:
        d1 = randint(1,6)
        d2 = randint(1,6)
        contador+=1
        if d1 == d2: break
    return contador

def ex4(string,letra,n):
    i = 0
    index = 0
    while i<n:
        index = str.find(string,letra,index+1)
        i+=1
    return index

def ex5(n):
    fibonacci = [0]
    i = 1
    while i<n:
        if i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        i+=1
    return sum(fibonacci),fibonacci

def ex6(n):
    fatorial = 1
    while n>1:
        fatorial*=n
        n-=1
    return fatorial

def ex7(n):    
    from math import sqrt
    if n<=1:
        return False
    i = 2
    while i<=sqrt(n):
        if (n % i == 0):
            return False
        else:
            i+=1
    return True

def ex8(lista):
    lista.sort()
    N = 1
    while lista[N-1]==N:
        N+=1
    return N
        