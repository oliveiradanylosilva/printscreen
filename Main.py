import pyautogui
import time
from  datetime import date 
import os

'''

O Programa irá criar uma pasta com o dia atual, acessar 3 Urls, printar a tela dos 3 sites acessados e salvar os arquivos dentro da pasta do dia atual com o nome do site+data. 

'''

data_atual = str(date.today()) #cria a data atual e transforma em string para ser usada no nome da pasta.

#Seleção de período de execução

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
diretorio = (f"C:\\{data_atual}-{periodo}\\") 
#diretorio = (f"C:\\Users\\seu_usuario\\Pictures\\{data_atual}-{periodo}\\") 

os.makedirs(diretorio,exist_ok=True) # Cria o diretório com o nome da pasta.'

       
#Definir os links que desejam que sejam printados.

link_1  = "https://www.globo.com"
link_2 =  'https://www.youtube.com.br'
link_3 =  'https://www.uol.com.br'

pyautogui.hotkey("win","r")
pyautogui.write("chrome --start-maximized")
pyautogui.press("enter")
time.sleep(1)

#print1
pyautogui.write(link_1)
pyautogui.press("enter")
time.sleep(5)

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
pyautogui.hotkey("alt","F4") 

print(f'Execução concluída com sucesso.Prints salvos no diretório: {diretorio}')
#saída do terminal com conclusão da execução
