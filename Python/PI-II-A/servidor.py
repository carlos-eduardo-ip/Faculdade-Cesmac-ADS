# import socket
from socket import *

host = 'localhost'
port = 50000

print(f'Servidor: {host}, conectado na Porta {port}!')

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind((host, port))
servidor.listen(1)
con, addr = servidor.accept()
print(f"Cliente {addr} se conectou!")

# Variaveis 
valor_cliente = 0
falha = 0
f = 'utf-8'
op_menu = 0


#Tela de login - Autenticação
def inicio():
    logado = False
    soma = 0
    global op_menu
    while logado == False:

        login = con.recv(1024).decode()
        senha = con.recv(1024).decode()
        if login == 'teste' and senha == 'teste':
            logado = True
            sucesso = 'logado com sucesso'
            con.send(sucesso.encode())
            break
        elif login != 'teste' and senha != 'teste':
            falha = 'Falha na autenticação. Tente novamente!'
            con.send(falha.encode())
            soma += 1
        elif soma == 3:
            break
        else: 
            falha = 'Falha na autenticação. Tente novamente!'
            con.send(falha.encode())
            soma +=  1

def menu():
    inicio()
    global valor_cliente, falha, op_menu
    while True:
        op_menu = con.recv(1024).decode(f)
        op_menu = int(op_menu)

        if op_menu == 1:
            valor = con.recv(1024).decode(f)
            valor = float(valor)
            valor_cliente = valor_cliente + valor
            con.send(str(valor_cliente).encode(f))
        elif op_menu == 2:
            valor = con.recv(1024).decode(f)
            valor = float(valor)
            falha = valor_cliente - valor
            if falha >= 0:
                valor_cliente = falha
                con.send(str(valor_cliente).encode(f))
            else:
                con.send(str(falha).encode(f))
        elif op_menu == 3:
            servidor.close()
            break
menu()