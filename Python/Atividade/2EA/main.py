from arvoreController import ArvoreBinariaController

arvore_controller = ArvoreBinariaController()

arvore_controller.inserir(50)
arvore_controller.inserir(30)
arvore_controller.inserir(70)
arvore_controller.inserir(20)
arvore_controller.inserir(40)
arvore_controller.inserir(60)
arvore_controller.inserir(80)

print("Em Ordem:")
arvore_controller.mostrar_em_ordem()

print("Pré Ordem:")
arvore_controller.mostrar_pre_ordem()

print("Pós Ordem:")
arvore_controller.mostrar_pos_ordem()

arvore_controller.remover(20)
arvore_controller.remover(30)
arvore_controller.remover(70)

print("Após remoção:")
arvore_controller.mostrar_em_ordem()

