from arvoreController import ArvoreBinariaController
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    controller = ArvoreBinariaController()

    # Adicionando pessoas à fila de espera
    controller.adicionar_pessoa_fila_espera("João", 45, 5)
    controller.adicionar_pessoa_fila_espera("Maria", 70, 0)
    controller.adicionar_pessoa_fila_espera("Pedro", 35, 0)
    controller.adicionar_pessoa_fila_espera("Ana", 62, 0)
    controller.adicionar_pessoa_fila_espera("Luiza", 28, 5)
    controller.adicionar_pessoa_fila_espera("Carlos", 55, 5)
    controller.adicionar_pessoa_fila_espera("Paula", 40, 0)

    while True:
        print("\n### MENU ###")
        print("1. Adicionar à fila de espera")
        print("2. Informar o próximo que será atendido")
        print("3. Mostrar fila de espera")
        print("4. Remover da fila de espera")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
          case 1:
              nome = input("Digite o nome da pessoa: ")
              idade = int(input("Digite a idade da pessoa: "))
              prioritario = input("A pessoa é prioritária? (S/N): ").upper() == "S"
              prioridade = 0 if prioritario else 5
              controller.adicionar_pessoa_fila_espera(nome, idade, prioridade)
              print(f"{nome} foi adicionado à fila de espera.")
              time.sleep(1)
              clear()
          case 2:
              clear()
              controller.informar_proximo_atendimento()
          case 3:
              clear()
              print("\n### FILA DE ESPERA ###")
              controller.mostrar_fila_espera()
          case 4:
                numero_fila = int(input("Informe o número a ser removido da fila: "))
                clear()
                controller.remover_pessoa_fila_espera(numero_fila)
          case 5:
              print("Saindo...")
              time.sleep(1)
              clear()
              break
          case _:
              print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":

    menu()
