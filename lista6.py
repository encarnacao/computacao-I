# -*- coding: utf-8 -*-
"""
Lista 6 de Comp 1
"""

def ex1(frase):
    lista = frase.split()
    lista.reverse()
    return ' '.join(lista)

def ex2(frase):
   lista = frase.split()
   lista.sort()
   return ' '.join(lista)

def ex3(frase):
    a = frase.replace('a','i')
    b = a.replace('e','i')
    c = b.replace('o','i')
    d = c.replace(' u','i')
    return d

def ex4(frase,palavra,posicao):
    lista = frase.split()
    if palavra in lista:
        lista[lista.index(palavra)] = lista[lista.index(palavra)].upper()
    else:
        lista.insert(posicao,palavra)
    return ' '.join(lista)

def ex5(lista):
    return sum(lista[0][2])+sum(lista[1][2])+sum(lista[2][2])

def ex6(lista,numero):
    lista.append(numero)
    lista.sort()
    return lista

def ex7(lista,n):
    if n in lista:
        return lista[:lista.index(n)+1]
    else:
        lista.append(n)
        lista.sort(reverse=True)
        return lista[:lista.index(n)]
    
def ex8(lista):
    lista.sort(reverse=True)
    return lista.pop(0)

def ex9(lista):
    media = sum(lista)/len(lista)
    acima = ex7(lista,media)
    return media,acima
           
def ex10(lista,H,L):
    if (lista[0]<= H and lista[1] <=L) or (lista[0]<=L and lista[1]<= H):
        return True
    elif  (lista[0]<= H and lista[2] <=L) or (lista[0]<=L and lista[2]<= H):
        return True
    elif  (lista[1]<= H and lista[2] <=L) or (lista[1]<=L and lista[2]<= H):
        return True
    else:
        return False
