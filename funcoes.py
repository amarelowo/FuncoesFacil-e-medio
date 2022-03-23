from cmath import pi
from math import sqrt


def radGraus(rad):
    graus = rad * 180 /pi
    return round(graus,1)

def Converter(h):
    mes = round(h / 720)
    sem = round(h/168)
    minu = h*60
    sec = h*3600
    milisec = h*3600*1000
    lista = [mes, sem, minu, sec, milisec]
    return lista

def repetir(item, n):
    lista = []
    for i in range(0, n):
        lista.append(item)

    return lista

def contaUm(n):
    cont = 0
    binario = str(bin(n))
    for i in range(len(binario[2:])):
        if binario[i] == '1':
            cont = cont + 1
    return cont

def distancia(a,b):
    dist = sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    return round(dist,2)

def cross_bots(n):
    if n%3 == 0 and n%5 != 0:
        r = "Cross"
    elif n%3 != 0 and n%5 == 0:
        r = "Bots"
    elif n%3 == 0 and n%5 == 0:
        r = "CrossBots"
    else: 
        r = str(n)

    return r