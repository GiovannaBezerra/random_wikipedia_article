# Random Wikipedia Article using Python
# The program searches Wikipedia and fetches a random article. 
# Then it asks the user if he wants to read that article or not. If the answer is yes, the material is shown; 
# otherwise, another random report is presented.

#Fonte:
#https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

#importando módulos
import requests
from bs4 import BeautifulSoup
import webbrowser
import time

#Busca um artigo aleatório da Wikipedia:
html_content = requests.get('https://en.wikipedia.org/wiki/Special:Random').content

#Obtem o conteúdo HTML da url apontada randomicamente:
soup = BeautifulSoup(html_content,'html.parser')

#Obtem o título do artigo:
article_title = soup.title.string.replace(' - Wikipedia','')

#Obtem um resumo (quando existir) do artigo com os cem primeiros caracteres:
summary = soup.find("p").text

#Pergunta ao usuário se ele gostaria de ler um artigo da Wikipedia:
print('\nOlá, você gostaria de ler o seguinte artigo na Wikipedia?\n')
print(article_title)
print('Resumo:')
print(summary[0:100]+"...")

#Capta a resposta do usuário:
user_option = input('\nPor favor preencha com S ou N:\n ')

#Verifica se o usuário tem interesse no artigo indicado e, caso positivo abre o link do mesmo e, caso negativo abre um artigo aleatório na Wikipedia:
if user_option.upper() == 'S':
    link_wikipedia = 'https://en.wikipedia.org/wiki/'+ article_title
    print('Boa escolha!')
    time.sleep(2)
    webbrowser.open(link_wikipedia)
else:
    print('\nQue pena! Espero que este outro artigo seja do seu interesse então...')
    time.sleep(2)
    webbrowser.open('https://en.wikipedia.org/wiki/Special:Random')