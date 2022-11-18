# Random Wikipedia Article using Python
# The program searches Wikipedia and fetches a random article. 
# Then it asks the user if he wants to read that article or not. If the answer is yes, the material is shown; 
# otherwise, another random report is presented.

# Fonte:
# https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

# Importando módulos:
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import PySimpleGUI as sg

# Busca um artigo aleatório da Wikipedia:
html_content = requests.get('https://en.wikipedia.org/wiki/Special:Random').content

# Capta o conteúdo HTML da url apontada:
soup = BeautifulSoup(html_content,'html.parser')

# Capta o título do artigo:
article_title = soup.title.string.replace(' - Wikipedia','')

# Capta o resumo (quando existir) do artigo considerando os cem primeiros caracteres:
summary = soup.find("p").text

# Pergunta ao usuário se ele gostaria de ler um artigo da Wikipedia usando PySimpleGUI:

# Escolhe o tema da janela:
sg.theme('DarkAmber')

# Define o layout da janela:
layout = [[sg.Text('Você gostaria de ler o seguinte artigo na Wikipedia?')],
          [sg.Text('Título: ' + article_title)],
          [sg.Text('Resumo: ' + summary[0:100]+"...")],
          [sg.Text(size=(50,1),key='-OUTPUT-')],
          [sg.Button('Sim'),sg.Button('Não'),sg.Button('Cancelar')]]

# Cria a janela:
window = sg.Window('Sugestão de leitura',layout)

# Apresenta a sugestão de leitura do artigo ao usuário usando um loop:
while True:
    event, values = window.read()
    # Opção para encerrar o loop se o usuário fechar a janela ou clicar em 'Cancelar':
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    # Abre o link correspondente caso o usuário clique em 'Sim':
    elif event == 'Sim':
        window['-OUTPUT-'].update('Boa leitura!',text_color='white')
        link_wikipedia = 'https://en.wikipedia.org/wiki/'+ article_title
        webbrowser.open(link_wikipedia)
    # Abre um link aleatório caso o usuário clique em 'Não':
    else:
        window['-OUTPUT-'].update('Que pena! Espero que este outro artigo seja do seu interesse.',text_color='white')
        webbrowser.open('https://en.wikipedia.org/wiki/Special:Random')
    
time.sleep(3)

# Fecha a janela:
window.close()