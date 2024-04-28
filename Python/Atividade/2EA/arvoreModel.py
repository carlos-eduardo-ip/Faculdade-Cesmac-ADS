from No import No

class ArvoreBinariaModel:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no.esquerda)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no.direita)

    def remover(self, valor):
        self.raiz = self._remover_recursivo(valor, self.raiz)

    def _remover_recursivo(self, valor, no):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover_recursivo(valor, no.esquerda)
        elif valor > no.valor:
            no.direita = self._remover_recursivo(valor, no.direita)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            
            temp = self._min_valor_no(no.direita)
            no.valor = temp.valor
            no.direita = self._remover_recursivo(temp.valor, no.direita)
        
        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

