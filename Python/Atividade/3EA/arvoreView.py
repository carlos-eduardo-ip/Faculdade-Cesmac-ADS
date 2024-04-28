class ArvoreBinariaView:
    def mostrar_em_ordem(self, no):
        if no:
            self.mostrar_em_ordem(no.esquerda)
            print(f"Nome: {no.nome}, Idade: {no.idade}, Prioritário: {no.prioritario}")
            self.mostrar_em_ordem(no.direita)
            