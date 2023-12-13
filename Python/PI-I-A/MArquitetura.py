import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

def buscarURL(text: int):

    # Fazer a solicitação HTTP
    match text:
        case 1:
            url = 'https://pt.wikipedia.org/wiki/Arquitetura_de_computadores#:~:text=A%20evolu%C3%A7%C3%A3o%20da%20inform%C3%A1tica%20foi,r%C3%ADgido%2C%20a%20exist%C3%AAncia%20de%20mem%C3%B3ria'
        case 2:
            url = 'https://pt.wikipedia.org/wiki/Componente_eletr%C3%B4nico'
        case 3:
            url = 'https://pt.wikipedia.org/wiki/Armazenamento_de_dados_de_computador'
        case 4:
            url = 'https://pt.wikipedia.org/wiki/Entrada/sa%C3%ADda'
        case 5:
            url = 'https://pt.wikipedia.org/wiki/Programa_de_computador'

    response = requests.get(url)

    # Analisar o conteúdo HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar a classe HTML desejada e obter o texto
    my_class = soup.find('div', {'class': 'mw-parser-output'})
    textURL = my_class.text.strip()

    return textURL
    


def menuArquitetura():

    sg.theme('Reddit')
    
    col1 = [[sg.Text('Escolha a opção desejada:', size=(22, 1), font=10)],
        [sg.Button('1 - Arquitetura de computadores', size=(33,0))],
        [sg.Button('2 - Componente eletrônico', size=(33,0))],
        [sg.Button('3 - Armazenamento de dados de computador', size=(33,0))],
        [sg.Button('4 - Entrada/saída', size=(33,0))],
        [sg.Button('5 - Programa de computador', size=(33,0))],
        [sg.Button('Sair', size=(5, 0), font=(10), pad=(5, 0))]]

    col2 = [[sg.Multiline(key='-OUTPUT-', size=(60, 20))]]

    layout = [[sg.Column(col1,justification='left'), sg.Column(col2)]]
        

    menuSO = sg.Window('Wiki - Programação', layout=layout)


    while True: 
        eventos, valores = menuSO.read()
        if eventos in (sg.WIN_CLOSED, 'Sair'):
            break
        else:
            if eventos == '1 - Arquitetura de computadores':
                text = 1
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)
            elif eventos == '2 - Componente eletrônico':
                text = 2
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)
            elif eventos == '3 - Armazenamento de dados de computador':
                text = 3
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)
            elif eventos == '4 - Entrada/saída':
                text = 4
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)
            elif eventos == '5 - Programa de computador':
                text = 5
                textURL = buscarURL(text)
                menuSO['-OUTPUT-'].update(textURL)
            
    menuSO.close()


