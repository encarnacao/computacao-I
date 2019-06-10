def ls1(a,b):
    return a + b + b + a

def lucky(x):
    return (x*4+8)*60/240 + 22 - x

def ls2(nome, idade):
    return "Parabéns " + nome + "! Seu número da sorte é " + str(int(lucky(idade))) + "!"

def ls3(st1,st2):
    if len(st1)<15 or len(st2)<15:
        return "String deve ter no mínimo 15 caracteres"
    else:
        st2_end = len(st2)-10
        return st1[5:]+st2[:st2_end]

def ls4(s,x,i):
    if len(s) == 0:
        return 'String s vazia'
    elif i<0 or i>len(s)-1:
        return "O valor de i deve estar entre 0 e " + str(int(len(s)-1))
    else:
        return s[:i] + x + s[i+1:]

def smean(x):
    return len(x)//2

def ls5(string):
    return string[:smean(string)] + string + string[smean(string):]

def ls6(st):
    return '#'+st[:smean(st)]+'#'+st[smean(st):]+'#'

def ls7(s):
    if len(s)<3:
        return 'String deve ter no mínimo 3 caracteres'
    pos = len(s)-3
    return s[-3:]+s[:pos]

def ls8(s,x):
    if len(s)<x:
        return 'String deve ter no mínimo ' + str(x) + ' caracteres'
    pos = len(s)-x
    return s[pos:]+s[:pos]

def ls9(s,x):
    pos = len(s)-x
    return s[pos:]+s[:pos]

def ls10(data1,data2):
    dias1 = int(data1[:2])
    dias2 = int(data2[:2])

    mes1 = int(data1[3:5])
    mes2 = int(data2[3:5])

    ano1 = int(data1[6:])
    ano2 = int(data2[6:])
    return (ano2*365 + mes2*30 + dias2)-(ano1*365 + mes1*30 + dias1)
