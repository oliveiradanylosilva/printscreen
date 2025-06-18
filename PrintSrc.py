import pyautogui
import time
from  datetime import date 
import os

'''

O Programa irá criar uma pasta com o dia atual, acessar 3 Urls, printar a tela dos 3 sites acessados e salvar os arquivos dentro da pasta do dia atual com o nome do site+data. 

'''

data_atual = str(date.today()) #cria a data atual e transforma em string para ser usada no nome da pasta.
#data_atual = str(data_atual)

def selecionar_horario():
    while True:
        print("Escolha uma opção:")
        print("1.Abertura")
        print("2.Fechamento")
        escolha = input("Digite o número da opção: ")

        if escolha == '1':  
            escolha = "Abertura"    
            break  
        elif escolha == '2':
            escolha = "Fechamento"
            break
        else:
            print("Opção inválida, digite 1 ou 2")
    return escolha

periodo = selecionar_horario()
diretorio = (f"C:\\Users\\olive\\Pictures\\{data_atual}-{periodo}\\") 

os.makedirs(diretorio,exist_ok=True) # Cria o diretório com o nome da pasta.'

        

#os.mkdir("C:\\Users\\olive\\Pictures\\"+data_atual) # Cria o diretório com o nome da pasta.


#definir os links que desejam que sejam printados.

link_1  = "https://www.globo.com"
link_2 =  'https://www.youtube.com.br'
link_3 =  'https://www.uol.com.br'

#Defina o diretório onde serão salvos 

#diretorio = (f"C:\\Users\\olive\\Pictures\\{data_atual}\\") 

#pyautogui.sleep = 0.4
pyautogui.hotkey("win","r")
pyautogui.write("chrome --start-maximized")
pyautogui.press("enter")
time.sleep(1)

#print1
pyautogui.write(link_1)
pyautogui.press("enter")
time.sleep(5)
#pyautogui.click(x=1318, y=35) [v1.0]-Remoção do clique de maximixar para solução de start maaximized na linha 31. para uso em demais de resoluções de tela.
pyautogui.sleep(3)
pyautogui.screenshot(f"{diretorio}PrintGlobo-{data_atual}.png")
time.sleep(1)

#print2
pyautogui.hotkey('ctrl','t')
pyautogui.write(link_2)
pyautogui.press("enter")
time.sleep(10)
pyautogui.screenshot(f"{diretorio}PrintYoutube-{data_atual}.png")

#print3
pyautogui.hotkey('ctrl','t')
pyautogui.write(link_3)
pyautogui.press("enter")
time.sleep(10)
pyautogui.screenshot(f"{diretorio}PrintUol-{data_atual}.png")
time.sleep(2)

#CloseChrome
pyautogui.hotkey("alt","F4") # [v1.0] - remoçao do click para execução em demais resoluções.

#pyautogui.click(x=1880, y=29)


#1 - Abrir o Chrome - ok
#2 - Digitar as Urls - ok 
#3 - Printar cada umas das Urls - ok
#4 - Salvar em uma pasta com o dia atual do print - ok 
#5 - possibilidade de uma validação do horário de execução, visto que será executado duas vezes ao dia inicio e fim.OK
#6 - validação de except quando a pasta já existir, com uma condição de escolha para  sobrepor ou deletar a pasta já existente. OK utilizado oks.mkdirs, ignorando pasta existente.

#To Do - 06062025
#3 transformar em executável. 

