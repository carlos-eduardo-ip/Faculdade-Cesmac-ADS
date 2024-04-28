import os
import time
from collections import deque

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

def filaDeEspera(fila, matricula, nome, lista_de_espera):
    aluno = Aluno(matricula, nome)
    fila.append((aluno, lista_de_espera))

def cadastrarAlunoFila(lista_alunos):
    if lista_alunos:
        matricula = lista_alunos[-1][0].matricula + 1
        proximo_numero_fila = max(aluno[1] for aluno in lista_alunos) + 1
        lista_de_espera = proximo_numero_fila
    else:
        matricula = 1
        lista_de_espera = 1
    
    nome = input("Digite o nome do aluno: ")
    filaDeEspera(lista_alunos, matricula, nome, lista_de_espera)
    print("Aluno adicionado à fila de espera.")
    time.sleep(1)
    clear()

def removerAlunoDaFila(lista_alunos):
    if lista_alunos:
        aluno = lista_alunos.popleft()[0]
        print(f"Cadastrando: Matrícula: {aluno.matricula} | Aluno {aluno.nome}")
        time.sleep(1)
        clear()
        for i, (aluno, _) in enumerate(lista_alunos):
            lista_alunos[i] = (aluno, i + 1)
    else:
        print("Não há alunos na fila de espera.")
        time.sleep(1)
        clear()
        

def mostrarFilaDeEspera(lista_alunos):
    print("\n### LISTA DE ESPERA ###")
    if lista_alunos:
        for index, (aluno, lista_de_espera) in enumerate(lista_alunos, start=1):
            print(f"Fila de espera: {lista_de_espera} | Matrícula: {aluno.matricula} | Nome: {aluno.nome}")
    else:
        print("Nenhum aluno cadastrado.")
    time.sleep(2)
    clear()

def menu():
    lista_alunos = deque()

    while True:
        print("\n### MENU ###")
        print("1. Adicionar aluno à fila de espera")
        print("2. Cadastrar próximo aluno")
        print("3. Mostrar fila de espera")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
          case 1:
            clear()
            cadastrarAlunoFila(lista_alunos)
          case 2:
            removerAlunoDaFila(lista_alunos)
          case 3:
             mostrarFilaDeEspera(lista_alunos)
          case 4:
              print("Saindo...")
              time.sleep(1)
              clear()
              break
          case _:
              print(f"Opção inválida. Por favor, escolha uma opção válida.")
              time.sleep(1)
              clear()

menu()
