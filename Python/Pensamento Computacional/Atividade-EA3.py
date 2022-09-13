import os
from time import sleep
from funcoes import caixa_eletronico

# Valores retirados no site https://mercado.carrefour.com.br/mercearia

nome = ''


def Recepção():
    global nome
    print('Seja bem vindo ao Supermercado IP')
    nome = input('Qual é o seu nome?\n')
    os.system('cls')
    sleep(0.5)
    return nome


Recepção()
soma = caixa_eletronico()
sleep(1.5)
os.system('cls')


if soma == 0:
    print(f'{nome}, infelizmente não foi hoje! Mas, é sempre um prazer te atender.\nVolte sempre e muito obrigado pela confiança!')
    sleep(2)
else:
    print(f'Total das compras: R$ {soma}')
    print(f'{nome}, é uma alegria ter um cliente como você. Nós nos dedicamos ao máximo, porque temos você ao nosso lado!\nObrigado pela preferência!')
    sleep(2)
