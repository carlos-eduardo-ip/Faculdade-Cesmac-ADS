from arvoreModel import ArvoreBinariaModel

class ArvoreBinariaController:
    def __init__(self):
        self.model = ArvoreBinariaModel()

    def adicionar_pessoa_fila_espera(self, nome, idade, prioridade):
        if prioridade < 0:
            prioridade = 0
        elif prioridade > 5:
            prioridade = 5
        
        self.model.adicionar_pessoa_fila_espera(nome, idade, prioridade)

    def informar_proximo_atendimento(self):
        self.model.informar_proximo_atendimento()

    def mostrar_fila_espera(self):
        self.model.mostrar_fila_espera()
    
    def remover_pessoa_fila_espera(self, fila_espera):
        self.model.remover_pessoa_fila_espera(fila_espera)
