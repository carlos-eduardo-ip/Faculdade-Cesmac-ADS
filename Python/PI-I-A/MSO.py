import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup


def buscarURL(text: int):

    # Fazer a solicitação HTTP
    match text:
        case 1:
            url = 'https://pt.wikipedia.org/wiki/Sistema_operativo'
        case 2:
            url = 'https://pt.wikipedia.org/wiki/Software'
        case 3:
            url = 'https://pt.wikipedia.org/wiki/Hist%C3%B3ria_do_hardware'
        case 4:
            url = 'https://pt.wikipedia.org/wiki/Thread_(computa%C3%A7%C3%A3o)#:~:text=Thread%20(em%20portugu%C3%AAs%3A%20fio%20de,concorrentemente%20(%22simult%C3%A2neo%22).'
        case 5:
            url = 'https://pt.wikipedia.org/wiki/Gerenciamento_de_mem%C3%B3ria'

    response = requests.get(url)

    # Analisar o conteúdo HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar a classe HTML desejada e obter o texto
    my_class = soup.find('div', {'class': 'mw-parser-output'})
    textURL = my_class.text.strip()

    return textURL
    

def menuSO():

    sg.theme('Reddit')
    
    col1 = [[sg.Text('Escolha a opção desejada:', size=(22, 1), font=10)],
        [sg.Button('1 - História dos Sistemas Operacionais')],
        [sg.Button('2 - Revisão de Software')],
        [sg.Button('3 - Revisão de Hardware')],
        [sg.Button('4 - Conceitos de Threads')],
        [sg.Button('5 - Gerenciamento de memória')],
        [sg.Button('Sair', size=(5, 0), font=(10), pad=(5, 0))],]

    col2 = [[sg.Multiline(key='-OUTPUT-', size=(60, 20))]]

    layout = [[sg.Column(col1), sg.Column(col2)]]

    menuSO = sg.Window('Wiki - Programação', layout=layout)

    while True: 

        eventos, valores = menuSO.read()

        if eventos in (sg.WIN_CLOSED, 'Sair'):
            break
        else:

            if eventos == '1 - História dos Sistemas Operacionais':
                text = 1
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)

            elif eventos == '2 - Revisão de Software':
                text = 2
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)

            elif eventos == '3 - Revisão de Hardware':
                text = 3
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)

            elif eventos == '4 - Conceitos de Threads':
                text = 4
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)
                
            elif eventos == '5 - Gerenciamento de memória':
                text = 5
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)
            
    menuSO.close()
