"""1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);"""
indice, soma, k = 13, 0, 0

while k < indice:
    k = k + 1
    soma = soma + k
print ("O valor da variável soma é "+str(soma))