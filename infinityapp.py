from mensagem import *
from os import system
from pyautogui import press, locateOnScreen, hotkey
from time import sleep

#Limpar o começo e mudar sua cor
system('color 1')
bruto = ''
system('cls')

#função pra dividir os blocos de código
def criarDivisao():
    print('=-='*18)

while bruto != '.':
    criarDivisao()
    try:
        bruto = input("Informações Infinity App: ")
        criarMensagem(bruto)
        while not locateOnScreen('campoMensagem.png'):
            sleep(1)
        hotkey('ctrl', 'v')
        sleep(0.5)
        press('enter')
        continuar = input("Criar mais um aluno?(S/N)")
        if(continuar.upper()=='S'):
            pass
        elif(continuar.upper()=='N'):
            break
    except:
        system('cls')
        print("insira uma informação valida")
