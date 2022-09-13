import os
from time import sleep
produtos_mercado = [0, 16.69, 9.49, 13.19, 3.48, 6.02]
soma = 0

def mercearia():
    print('Produtos disponível: ')
    print('1 - Café Almofada Extra Forte 3 Corações 500G - R$ 16,69')
    print('2 - Óleo de Soja Concordia 900ml - R$ 9,49')
    print('3 - Pipoca Pronta Doce Caramelizada Cheetos 140g - R$ 13,19')
    print('4 - Chocolate ao Leite com Confeitos de Chocolate Garoto Cores - 90g - 3,48')
    print('5 - Extrato de Tomate Elefante 310g - R$ 6,02')

def caixa_eletronico():
    global produtos_mercado
    global soma

    while True:
        mercearia()
        try:
            menu = int(input('\nDigite o número do produto que deseja comprar: '))
            soma = produtos_mercado[menu]
        except IndexError:
            print('Esse produto não está disponível no momento.\n Por favor, selecione um produto disponível!')
            sleep(1.5)
            os.system('cls')
            continue
        else:
            cliente = input('\nDeseja continuar comprando? Sim ou Não \n')
            if cliente == 'sim' or cliente == 'Sim':
                soma += soma
                os.system('cls')
                sleep(0.5)
            else:
                soma += soma
                break
    return soma