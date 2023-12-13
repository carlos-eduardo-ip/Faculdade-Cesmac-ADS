import PySimpleGUI as sg
from MSO import *
from MArquitetura import *

def menu():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text('Escolha a opção desejada:', size=(22, 1), font=10)],
        [sg.Button('1 - Arquitetura e Organização de Computadores', size=(35,0))],
        [sg.Button('2 - Sistemas Operacionais', size=(35,0))],
        [sg.Button('Sair', size=(5, 0), font=(10), pad=(5, 0))]]
  

    menu = sg.Window('Wiki - Programação', layout=layout, finalize=True, auto_size_buttons=True, element_justification='center')
    
    while True: 
        eventos, valores = menu.read()
        if eventos in (sg.WIN_CLOSED, 'Sair'):
            break
        else:
            if eventos == '1 - Arquitetura e Organização de Computadores':
                menu.hide()
                menuArquitetura()
                menu.un_hide()
            elif eventos == '2 - Sistemas Operacionais':
                menu.hide()
                menuSO()    
                menu.un_hide()

    menu.close()    

menu()
