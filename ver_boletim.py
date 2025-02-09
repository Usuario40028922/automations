import glob
from operator import indexOf
from re import S
from tkinter import N
import pyautogui as pa
from time import sleep
from subprocess import run

primeira_vez = True

def academico():
    run([r'C:\Program Files\Mozilla Firefox\firefox.exe'])
    sleep(2)
    pa.hotkey("ctrl", "t")
    sleep(0.5 )
    pa.write('iff academico')
    pa.press("enter")
    sleep(3)
    pa.click(x=366, y=417)
    sleep(2)
    pa.click(x=1112, y=246)
    sleep(1)
    pa.click(x=600, y=351)
    pa.write('20241040030')
    sleep(1)
    pa.press('tab')
    sleep(1)
    pa.write('ian09042009')
    sleep(1)
    pa.click(x=858, y=353)
    sleep(2)
    pa.press('tab')
    sleep(0.5)
    pa.press('tab')
    sleep(0.5)
    pa.press('tab')
    sleep(0.5)
    pa.press('tab')
    sleep(0.5)
    pa.press('enter')

def rewards():
  conjunto_diario = [(1758, 731), (1303, 730), (841, 553)]

  run([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge'])
  sleep(2)
  pa.hotkey("ctrl", "tab")
  sleep(1)
  pa.write("https://rewards.bing.com/")
  pa.press("enter")
  sleep(1)
  #29 - conjunto diário
  #32 - primeira tarefa, enter
  
  
  vez = 1
  for tab in range(38):
    pa.press("tab")
    sleep(0.1)
    if vez == 29:
      pa.click(conjunto_diario[0])
      sleep(2)
      pa.hotkey("ctrl", "w")
      sleep(0.5)
      pa.click(conjunto_diario[1])
      sleep(2)
      pa.hotkey("ctrl", "w")
      sleep(0.5)
      pa.click(conjunto_diario[2])
      sleep(2)
      pa.hotkey("ctrl", "w")
    elif vez >= 33:#tarefas diárias
        pa.press("enter")
        sleep(5)
        pa.hotkey("ctrl", "w")

    vez += 1

bots = {
  "iff_academico" : lambda : academico(),
  "microsoff_rewards" : lambda : rewards()
}

def _comandos(dic):
    for x, y in dic.items():
      print(f"\n#Comando \"{x}\"\n\tAção: {y}")

def _ajuda():
  print("Não irei ajudar.")

def _autobot():
  escolha = int(input("\nUsar um AUTO-BOT existente ou criar um novo?\n\t1 - Usar um AUTO-BOT ieiii!!11!!\n\t2 - Criar um novo.\n"))

  match escolha:
    case 1:
      a = [0, ]
      for x in bots:
        a[0] += 1
        print(f"{a[0]}° AUTOBOT - {x}")
        a.append(x)
      
      bot_escolhido = int(input("\nQual deseja?\n\t:- "))

      bots[a[bot_escolhido]]()
    


def _inpute():
  global primeira_vez
  
  descricoes = {
    "comandos" : "Lista todos os comandos possíveis.",
    "ajuda" : "Explica o propósito do algorítmo.",
    "autobot" : "Ativa o painel de bots."
  }

  comandos = {
    "comandos" : lambda: _comandos(descricoes),
    "ajuda" : _ajuda,
    "autobot" : _autobot 
  }

  if primeira_vez:
    print("\nJá que é sua primeira vez, tente o comando \"comandos\".")

    primeira_vez = False
  
  comanda = input("\nAtalho:\n\tcomando ação ação1...\n\nComando:- ").split()



  for comando in comandos:
    if comando == comanda[0]:
      comandos[comanda[0]]()
      break

'''
#pa.click(x=1143, y=243)
for x in range(2):
  sleep(2)
  print(pa.position())
pa.hotkey("ctrl", "t")
'''

#Início

while True:
  _inpute()
