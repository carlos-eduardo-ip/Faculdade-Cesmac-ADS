from collections import deque
from No import No

class ArvoreBinariaModel:
    def __init__(self):
        self.fila_espera = deque()
        self.numero_fila_atual = 0

    def adicionar_pessoa_fila_espera(self, nome, idade, prioridade):
        self.numero_fila_atual += 1
        numero_fila = self.numero_fila_atual
        self.fila_espera.append(No(nome, idade, prioridade, numero_fila))
        self.reordenar_fila()
        self.atualizar_numeros_fila()

    def informar_proximo_atendimento(self):
        if self.fila_espera:
            proximo = self.fila_espera.popleft()
            print(f"Próximo a ser atendido: {proximo.nome}")
            self.atualizar_numeros_fila()
        else:
            print("Não há ninguém na fila de espera.")

    def atualizar_numeros_fila(self):
        for i, pessoa in enumerate(self.fila_espera):
            pessoa.numero_fila = i + 1

    def reordenar_fila(self):
        self.fila_espera = deque(sorted(self.fila_espera, key=lambda x: (x.prioridade, x.numero_fila)))

    def mostrar_fila_espera(self):
        for pessoa in self.fila_espera:
            print(f" Número da fila: {pessoa.numero_fila} | Nome: {pessoa.nome}")

    def remover_pessoa_fila_espera(self, numero_fila):
        for pessoa in self.fila_espera:
            if pessoa.numero_fila == numero_fila:
                self.fila_espera.remove(pessoa)
                self.atualizar_numeros_fila()
                return print(f"{pessoa.nome} - Removido(a) da fila de espera")
