#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:57:54 2019

@author: cencarnacao
"""
def ex1(lista):
    l = []
    for i in range(len(lista)):
        l.append((lista[i],lista[i]))
    return list(dict.keys(dict(l)))

def ex2(numero):
    centenas = numero//100
    dezenas = (numero - centenas*100)//10
    unidades =numero-(centenas*100+dezenas*10)
    U = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    D ={0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9:'XC'}
    C ={0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8:'DCCC',9:'CM'}
    Romanos = {2:U,1:D,0:C}
    Numero = {0:centenas,1:dezenas,2:unidades}
    Resultado = ''
    i = 0
    while i<3:
        Resultado+=Romanos[i][Numero[i]]
        i+=1
    return Resultado

def romanos(numero):
    while len(numero)<3:
        numero = '0' + numero
    U = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    D ={0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9:'XC'}
    C ={0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8:'DCCC',9:'CM'}
    Romanos = {2:U,1:D,0:C}
    Resultado = ''
    for i in range(len(numero)):
        Resultado+=Romanos[i][int(numero[i])]
    return Resultado

def ex3(frase):
    lst_frase = frase.split()
    dicionario = []
    for i in range(len(lst_frase)):
        dicionario.append((lst_frase[i],lst_frase.count(lst_frase[i])))
    return dict(dicionario)

def ex4(aminoacido):
    RNA = {'UUU':'Phe','CUU':'Leu','UUA':'Leu','AAG':'Lisina','UCU':'Ser','UAU':'Tyr','CAA':'Gln'}
    traducao = ''
    for i in range(0,len(aminoacido),3):
        if i == 0: traducao += RNA[aminoacido[i:i+3]]
        else: traducao += '-' + RNA[aminoacido[i:i+3]]
    return traducao

def ex5(lista_de_compras,supermercado):
    preco = 0
    for i in lista_de_compras:
        if i in supermercado.keys():
            preco+=supermercado[i]
    return preco

def ex6(afinidades):
    reciprocidade = []
    afinidades = list(afinidades.items())
    for par in afinidades:
        if (par[1],par[0]) in afinidades:
            reciprocidade.append(par)
            del afinidades[afinidades.index(par)], afinidades[afinidades.index((par[1],par[0]))]
    return reciprocidade