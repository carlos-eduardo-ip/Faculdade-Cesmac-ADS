from arvoreModel import ArvoreBinariaModel
from arvoreView import ArvoreBinariaView

class ArvoreBinariaController:
    def __init__(self):
        self.model = ArvoreBinariaModel()
        self.view = ArvoreBinariaView()

    def mostrar_em_ordem(self):
        self.view.mostrar_em_ordem(self.model.raiz)
        print("\n")

    def mostrar_pre_ordem(self):
        self.view.mostrar_pre_ordem(self.model.raiz)
        print("\n")

    def mostrar_pos_ordem(self):
        self.view.mostrar_pos_ordem(self.model.raiz)
        print("\n")

    def inserir(self, valor):
        self.model.inserir(valor)

    def remover(self, valor):
        self.model.remover(valor)

