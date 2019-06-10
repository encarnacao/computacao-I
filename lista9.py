# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:32:40 2019

@author: Caio
"""

def ex1(matriz,numero):
    contador = 0
    for i in range(len(matriz)):
        contador += matriz[i].count(numero)
    return contador

def ex2(matriz):
    transposta = []
    for i in range(len(matriz[0])):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        transposta.append(linha)
    return transposta

def ex3(matriz):
    soma = 0
    quantidade = len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        soma+=sum(matriz[i])
    return soma/quantidade

def ex4(matriz):
    menor_tempo = 0
    jogador = 0
    volta = 0
    for i in range(len(matriz)):
        if i == 0:
            menor_tempo = min(matriz[i])
            jogador = i + 1
            volta = matriz[i].index(min(matriz[i])) + 1
        elif menor_tempo > min(matriz[i]):
            menor_tempo = min(matriz[i])
            jogador = i + 1
            volta = matriz[i].index(min(matriz[i])) + 1
    return ('Corredor ' + str(jogador),str(menor_tempo) + ' segundos',str(volta) + 'ª volta')

def ex5(matriz,setor):
    funcionarios = []
    for i in matriz:
        if setor in i:
            funcionarios.append(i[:2]+i[3:])
    if funcionarios == []:
        return 'Nenhum registro foi encontrado'
    return funcionarios

def ordenainsercao(lista):
    for i in range(1,len(lista)):
        while lista[i]<lista[i-1]:
            lista[i],lista[i-1] = lista[i-1],lista[i]
            if i != 1: i-=1
    return lista