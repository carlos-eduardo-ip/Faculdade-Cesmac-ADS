class ArvoreBinariaView:
    def mostrar_em_ordem(self, no):
        if no:
            self.mostrar_em_ordem(no.esquerda)
            print(no.valor, end=' ')
            self.mostrar_em_ordem(no.direita)
            
    def mostrar_pre_ordem(self, no):
        if no:
            print(no.valor, end=' ')
            self.mostrar_pre_ordem(no.esquerda)
            self.mostrar_pre_ordem(no.direita)

    def mostrar_pos_ordem(self, no):
        if no:
            self.mostrar_pos_ordem(no.esquerda)
            self.mostrar_pos_ordem(no.direita)
            print(no.valor, end=' ')

