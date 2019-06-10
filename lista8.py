# -*- coding: utf-8 -*-
"""
Lista 8 de Comp 1
@author: Caio
"""
def ex1(n):
    soma = 0
    for i in range(1,2*n+1,2):
        soma+=i
    return soma

def ex2():
    soma = 0
    for i in range(1,11):
        fatorial = 1
        for n in range(1,i+1):
            fatorial*=n
        soma+=fatorial
    return soma

def ex3(N):
    H = 0
    for i in range(N):
        H+=1/(i+1)
    return H

def ex4(n):
    soma = 0
    for i in range(n+1):
        soma+=(-1)**i/(2*i+1)
    return soma

def ex5(numero):
    count = 1
    for i in range(1,numero):
        if numero % i == 0:
            count+=1
    return count

def ex6(frase,letra):
    count = 0
    for char in frase:
        if char == letra: 
            count+=1
    return count

def ex7():
    def fat(n):
        fatorial = 1
        for i in range(1,n+1):
            fatorial*=i
        return fatorial
    soma = 0
    a = 10
    b = 1
    for i in range(10):
        soma+=(-1)**i*a/fat(b)
        a-=1
        b+=1
    return soma

def ex8(x,y):
    def primo(n): 
        if (n <= 1): 
            return False
        for i in range(2, n): 
            if (n % i == 0): 
                return False
        return True
    soma = 0
    for i in range(x,y+1):
        if primo(i): 
            soma+=i
    return soma

def ex9(n):
    soma_div = 0
    for i in range(1,n):
        if n % i == 0:
            soma_div+=i
    return soma_div == n

def ex10(palavra):
    for char in "aeiou":
        palavra = palavra.replace(char,char+'p'+char)
    return palavra

def ex11a(Qb,Dias):
    pop = Qb
    for i in range(Dias):
        pop*=2
    return pop
def ex11b(lista):
    pop, index = 0,0
    for i in lista:
        if ex11a(i[0],i[1])>pop:
            pop=ex11a(i[0],i[1])
            index = lista.index(i)
    return index,pop
