import random

#total de pontos gerados, que podem estar dentro ou fora do circulo
total_pontos = int(input("Qnt de pontos aleatorios que devem ser gerados:"))
pontos_cir = 0 #pontos que estão dentro do circulo de raio 1, ou seja, pontos que tem a distancia da origem menores que 1 d = sqrt((x-0^2)+(y-0)^2)

for i in range(total_pontos): #laço que gera pontos(x,y) aleatórios
    x = random.random() #função random.random() gera numeros aleatorios entre 0 e 1 (0<=n<1)
    y = random.random()

    if y**2+x**2 <= 1: #contando a quantidade de pontos dentro do circulo
        pontos_cir = pontos_cir + 1

pi = 4*pontos_cir/total_pontos       

print(pi)