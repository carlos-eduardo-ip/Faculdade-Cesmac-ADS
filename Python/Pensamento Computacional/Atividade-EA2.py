import os
from time import sleep

print('Seja bem vindo ao Supermercado IP')
produto = float(input('Digite o valor do produto: R$ '))
soma =  0 + produto
sleep(0.5)
os.system('cls')

while True:

    if produto <= 0:
        os.system('cls')
        break
    else:
        produto = float(input('Digite outro valor pra continuar ou 0 para encerrar: R$ '))
        soma += produto
        sleep(0.3)
        os.system('cls')

if soma == 0:
    print(f'Infelizmente não foi hoje! Mas, é sempre um prazer te atender.\nVolte sempre e muito obrigado pela confiança!')
    sleep(2)    
else:
    print(f'Total das compras: R$ {soma}')
    print(f'É uma alegria ter um cliente como você. Nós nos dedicamos ao máximo, porque temos você ao nosso lado!\nObrigado pela preferência!')
    sleep(2)
