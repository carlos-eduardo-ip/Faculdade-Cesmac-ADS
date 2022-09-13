import PySimpleGUI as sg
# import socket
from socket import *

host = 'localhost'
port = 50000

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((host, port))
#print(f'Conectado ao HOST [{host}] na PORTA {port}')

# Variaveis
f = 'utf-8'
Logado = False
op_menu = ''
valor_cliente = 0
falha = 0
valor = 0

def depositar():
    sg.theme('DarkGrey2')

    layout = [
        [sg.Text('Quanto deseja depositar:', size=(20, 1), font=15)],
        [sg.Text(''), sg.Input(key='-depositar-', font=16)],
        [sg.Button('Confirmar'), sg.Button('Voltar')]
    ]
    depositar = sg.Window("IP Bank", layout=layout, finalize=True)

    global valor_cliente
    while True:
        eventos, valores = depositar.read()
        if eventos == 'Voltar':
            op_menu = '0'
            cliente.send(op_menu.encode(f))
            valor_cliente = cliente.recv(1024).decode(f)
            break
        else:
            if eventos == 'Confirmar':
                cliente.send(valores['-depositar-'].encode())
                valor_cliente = cliente.recv(1024).decode()
                valor_cliente = float(valor_cliente)
                sg.popup(f'Valor em conta atualizado: R${valor_cliente:.2f}')
                break
    depositar.close()

def sacar():
    sg.theme('DarkGrey2')
    layout = [
        [sg.Text('Qauanto deseja sacar:', size=(20, 1), font=15)],
        [sg.Text(''), sg.Input(key='-sacar-', font=15)],
        [sg.Button('Confirmar'), sg.Button('Voltar')]
    ]
    sacar = sg.Window('IP Bank', layout=layout, finalize=True)
    global valor_cliente, falha
    while True:
        eventos, valores = sacar.read()
        if eventos == 'Voltar':
            op_menu = '0'
            cliente.send(op_menu.encode(f))
            valor_cliente = cliente.recv(1024).decode(f)
            break
        else:
            if eventos == 'Confirmar':
                cliente.send(valores['-sacar-'].encode())
                falha = cliente.recv(1024).decode()
                falha = float(falha)
                if falha >= 0:
                    valor_cliente = falha
                    sg.popup(f'Saldo atualizado: R${valor_cliente:.2f}')
                    break
                else:
                    sg.popup('Saldo insuficiente! Tente outro valor.')
                    op_menu = '2'
                    cliente.send(op_menu.encode())
    sacar.close()
    

# Janelas iniciais
def menu():
    sg.theme('DarkGrey2')
    
    layout = [
        [sg.Text('Escolha a opção desejada:', size=(22, 1), font=10)],
        [sg.Button('1 - Depositar', size=(20, 1), font=16)],
        [sg.Button('2 - Sacar', size=(20, 1), font=16)],
        [sg.Button('3 - Visualizar saldo', size=(20, 1), font=16)],
        [sg.Button('Sair', size=(5, 1), font=(10), pad=(70, 0))]]
  

    menu = sg.Window('Menu - IP Bank', layout=layout, finalize=True)
    global valor_cliente
    while True: 
        eventos, valores = menu.read()
        if eventos in (sg.WIN_CLOSED, 'Sair'):
            op_menu = '3'
            cliente.send(op_menu.encode(f))
            break
        else:
            if eventos == '1 - Depositar':
                op_menu = '1'
                cliente.send(op_menu.encode(f))
                menu.hide()
                depositar()
                menu.un_hide()
            elif eventos == '2 - Sacar':
                op_menu = '2'
                cliente.send(op_menu.encode(f))
                menu.hide()
                sacar()
                menu.un_hide()
            elif eventos == '3 - Visualizar saldo':
                valor_cliente = float(valor_cliente)
                sg.popup(f'Seu saldo atual é: R${valor_cliente:.2f}')    
    menu.close()    

 
def login():
    
    sg.theme('DarkGrey2')
    layout = [
        [sg.Text("Conecte-se", size =(15, 1), font=40)],
        [sg.Text("Nome: ", size = (15, 1), font=16),sg.InputText(key='-login-', font=16)],
        [sg.Text("Senha: ", size = (15, 1), font=16), sg.InputText(key='-senha-', password_char='*', font=16)],
        [sg.Button('Entrar'),sg.Button('Cancelar')]]

    login = sg.Window("IP BANK - Login", layout=layout, finalize=True)


    while True:
        eventos, valores = login.read()

        if eventos in (sg.WIN_CLOSED,'Cancelar'):
            break
        else:
            if eventos == 'Entrar':
                cliente.send(valores['-login-'].encode())
                cliente.send(valores['-senha-'].encode())
                msg = cliente.recv(1024).decode()
                
                if msg == 'logado com sucesso':
                    sg.popup("Seja Bem vindo ao IP Bank!")
                    login.hide()
                    menu()
                    break
                else:
                    sg.popup("Nome/Senha invalido. Tente novamente!")
    login.close()
login()
cliente.close()