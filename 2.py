"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo 
valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 
5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
avisando se o número informado pertence ou não a sequência."""

numero = int(input("Qual número você deseja realizar a consulta? "))
x, y = 0, 1
sequencia = []
while x < (numero+1):
    x, y = y, x+y
    sequencia.append(x)
for i in range(len(sequencia)):
    while sequencia[i] < numero:
        i += 1
    if sequencia[i] == numero:
        print("O número "+str(numero)+" faz parte da Sequência de Fibonnaci")
        break
    else:
        print("O número "+str(numero)+" não faz parte da Sequência de Fibonnaci")
        break
    