# Funcoes-Facil-e-medio

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
















