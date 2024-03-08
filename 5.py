"""5) Escreva um programa que inverta os caracteres de um string."""
palavra = input("Qual a palavra que você deseja reverter? ")
nova_palavra = ''
i = len(palavra)
while i > 0:
    nova_palavra = nova_palavra + (palavra[i-1])
    i-=1
print(nova_palavra)