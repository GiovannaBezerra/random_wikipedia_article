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

#Busca um artigo aleatório da Wikipedia:
html_content = requests.get('https://en.wikipedia.org/wiki/Special:Random').content

#Obtem o conteúdo HTML da url apontada randomicamente:
soup = BeautifulSoup(html_content,'html.parser')

#Obtem o título do artigo:
article_title = soup.title.string.replace(' - Wikipedia','')

#Obtem um resumo (quando existir) do artigo com os cem primeiros caracteres:
summary = soup.find("p").text