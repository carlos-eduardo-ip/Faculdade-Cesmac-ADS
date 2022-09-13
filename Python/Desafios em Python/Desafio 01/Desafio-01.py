from tkinter import *
from datetime import date

def calculateAge(ano): 
    today = date.today()
    age = today.year - ano.year - ((today.month, today.day) < (ano.month, ano.day)) 
    
    return age

def calculateDay(ano, mes, dia):
    today = date.today()
    data = date(ano, mes, dia)
    dias = abs(data - today)

    return dias.days

    

#Configurações da tela principal
janela = Tk()
janela.title("-- Desafio 01 --")
janela.iconbitmap(default="Desafios em Python/Desafio 01/Calculator_30001.ico")
janela.geometry("300x294+414+289") #Largura x Altura + distância esquerda + distância top



def clique_esq(retorno):
    print(f'X: {retorno.x} | Y: {retorno.y} Geo: {janela.geometry()}')


# Eventos e textos
janela.bind('<Button-1>', clique_esq)
texto_principal = Label(janela, text="Saiba a Idade atual de qualquer pessoa simplesmente \n introduzindo a sua data de nascimento: ")
texto_principal.grid(row=0, column=0)

confirmar = Button(janela, text="Calcular").grid(row=1, column=0)
sair = Button(janela, text="Sair", command=janela.destroy).grid(row=2, column=0)
janela.mainloop()