
# Random Wikipedia Article using Python
# The program searches Wikipedia and fetches a random article. 
# Then it asks the user if he wants to read that article or not. If the answer is yes, the material is shown; 
# otherwise, another random report is presented.

# Source:
# https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

# Imports libraries:
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import PySimpleGUI as sg

# Finds random article in Wikipedia:
html_content = requests.get('https://en.wikipedia.org/wiki/Special:Random').content

# Gets HTML content from url:
soup = BeautifulSoup(html_content,'html.parser')

# Gets article's title:
article_title = soup.title.string.replace(' - Wikipedia','')

# Gets article's summary (when it exist) seeing first one hundred characters:
summary = soup.find("p").text

# Asks the user if it would like to read an article from Wikipedia - using PySimpleGUI:

# Chooses the window theme:
sg.theme('DarkAmber')

# Defines the window layout:
layout = [[sg.Text('Would you like to read the following article from Wikipedia?')],
          [sg.Text('Title: ' + article_title)],
          [sg.Text('Summary: ' + summary[0:100]+"...")],
          [sg.Text(size=(50,1),key='-OUTPUT-')],
          [sg.Button('Yes'),sg.Button('No'),sg.Button('Cancel')]]

# Builds the window:
window = sg.Window('Read Suggestion',layout)

# Shows the user an article read suggestion - using a loop: 
while True:
    event, values = window.read()
    # It's an option to stop the loop if the user closes the window or clicks "Cancel":
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    # Open the link if the user clicks "Yes":
    elif event == 'Yes':
        window['-OUTPUT-'].update('Good reading!',text_color='white')
        link_wikipedia = 'https://en.wikipedia.org/wiki/'+ article_title
        webbrowser.open(link_wikipedia)
    # Open a random link if the user clicks "No": 
    else:
        window['-OUTPUT-'].update('Sorry! I hope this another article will be interesting for you.',text_color='white')
        webbrowser.open('https://en.wikipedia.org/wiki/Special:Random')
    
time.sleep(4)

# Close the window:
window.close()