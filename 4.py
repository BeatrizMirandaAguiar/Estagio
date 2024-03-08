"""4) Você está em uma sala com três interruptores, cada um conectado a uma 
lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que 
está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu 
objetivo é descobrir qual interruptor controla qual lâmpada. 
Como você faria para descobrir, usando apenas duas idas até uma das salas das 
lâmpadas, qual interruptor controla cada lâmpada? 

R.: Eu iria ligar o primeiro interruptor e esperaria um tempinho. Depois disso, 
iria desligá-lo, acender o segundo e iria para a primeira sala. Abaixo está 
o diagrama de possíveis casos:
Lâmpada acesa - interruptor 2
Lâmpada não acesa e quente - interruptor 1
Lâmpada não acesa e fria - interruptor 3

Após desvendar qual o interruptor da primeira sala, eu iria à segunda e 
verificaria o estado da lâmpada conforme descrito acima. Ao ter conhecimento 
de qual interruptor é o correspondente das primeiras 2 salas, o da terceira é 
descoberto por eliminação.
"""