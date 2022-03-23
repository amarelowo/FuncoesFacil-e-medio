# Documentação

Oi oi pessoal da Cross, uma observaçãozinha aqui, as funções retornam valores ou strings, então tem que usar o print(),
ou outra forma de apresenta-los. As os desafios de nível "muito fácil" até "medio"(exceto o Medio 3, codigo do robo) 
estão no mesmo arquivo("funcoes.py"). Só consegui fazer um dos desafios difíceis, o terceiro, da demonstração de pi. 

Muito Fácil --------------------------------------------------------------

1) função radGraus()

Recebe como parametro um certo valor em radianos
abre a varaivel "graus" e atribui a ela a equação que converte radianos em graus

(radianos * 180) / pi

Retorna a variavel "graus" com um arredendodamento de uma casa, através da função "round()"


2) Converter()

Recebe como paramentro um valor em horas
abre as variaveis mês("mes"), semana("sem"), minutos("minu"), segundos("sec") e minisegundos("milisec")
atribuindo a elas as devidas equações de conversão

Por ultima coloca todas a uma lista e a retorna


Fácil --------------------------------------------------------------

1) função repetir()

Recebe como parametro a string e o numero de vezes que sera repetida
Ex: repetir("Salve", 3)

Começa iniciando uma lista vazia, assim através do laço de repetição "for", acrescentará
a string solicitada um numero de vezes igual ao valor fornecido no inicio (Ex: 3)

Dentro dessa laço "for" é utilizado a função "range()", para delimitar quantas vezes o laço será
executado.

Assim retornando a lista obtida


2) função contaUm()

Recebe como parametro um certo numero inteiro decimal

Abre uma variavel "cont"(contador) e a varivel "binario" que recebe o valor do numero fornecido em binario no formato de string

str(bin(n)): bin() é para converter de decimal para binario, e a str() para transformar o numer em uma string(Ex: se recebeu 3, vira "0b11")

Então é aberto um "for" para percorrer a string gerada(do incidice 0 ao último)
Comparando o valor da string pertencendo naquele indice com "1", se forem iguais, o contador é incrementado (if binario[i] == "1")

retornando o valor do contador


Medio --------------------------------------------------------------

1) função distancia()

Recebe como parametro duas listas ou tuplas, que são equivalentes aos pontos que se deseja descobrir a distancia
Ex: a = (0, 0) e b = (1, 1), assim "distancia(a,b)" ou "distancia((0,0),(1,1))"

Abre uma variavel "dist"(distancia) e atribui a ela a equação de distancia entre dois pontos

Equação: sqrt( (X - Xo)^2 + (Y - Yo)^2 )

Retornando o valor da distancia arredondado em duas casas decimais(com a função round())


2) função cross_bots()

Recebe como parametro um numero decimal inteiro 

Abre uma cadeia de decisões que verifica se ele é multiplo de 3 (n%3 == 0 and n%5 != 0), atribui a string "Cross" à variavel "r"(retorno),
caso seja multiplo de 5 (n%3 != 0 and n%5 == 0), atribui "Bots" à variavel "r",
caso seja multiplo de ambos (n%3 == 0 and n%5 == 0), atribui "CrossBots"
casa nao, atribui o proprio valor inserido no formato de string

Obs: Nas comparações é utilizado o caracter "%" que significa resto da divisao pelo numero logo a frente, no caso "n%3 == 0"
"n"(numero fornecido) divido por 3 e comparando o restante da divisão com 0 (" == 0")

Retornando a string atribuida a "r" conforme o resultado da cadeia de decisões

Medio (codigo do robo sumo) -------------------------------------------------------------

Os componente são os preestabelecidos pelo site

A lógica se baseia em 4 senrores, 2 que monitoram o chão da arena e 2 que monitoram a distancia de qualquer objeto a sua frente

Tem uma aceleração constante dos motores, -10 e +10, propulsionando o robo para frente

Começa o loop com as variaveis "leftSpeed" e "rightSpeed" em 0, que mais adiante vão acelerar ou freiar o robo.

Tudo ocorre atráves de uma cadeia de dicisões, que comparam os valores fornecidos pelos sensores com um valor já preestabelecido:
Sensores de distancia: retornam um valor abaixo de 300 para objetos entre 0 e 300cm
Sensores de chão: retornam valores acima de 0.25 para mudança de "cor"(sinalizando que emcontrou a borda)


1°. se encontrar um objeto a direita => vire a direita

2°. se encontrar um objeto a esqueda => vire a esquerda

3°. se encontrar um objeto a frente => acelere
       dentro dessa condição possui uma outra
       se encontrar a borda => vire

4° se nao encontrar nada => gire em busca de algum objeto





