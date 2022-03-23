from tkinter import N


def contaUm(n):
    cont = 0
    binario = str(bin(n))
    print(binario)
    for i in range(len(binario)):
        if binario[i] == '1':
            cont = cont + 1
    return cont



m = int(input("Valor; "))
print(contaUm(m))