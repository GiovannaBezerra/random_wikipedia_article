<img src="https://user-images.githubusercontent.com/44107852/234053564-e2fda92f-5f46-44d7-b9b4-956ae824adb9.png" align="right"
      width="80" height="80">
      
# RANDOM WIKIPEDIA ARTICLE

*under construction*

This program searches Wikipedia and fetches a random article. Then it asks the user if he wants to read that article or not. If the answer is yes, the material is shown; otherwise, another random report is presented.

The aim of this project is to develop skills and materialize theoretical knowledge into practical experience.

<p align="center">
  <a href="#how-it-works">How it works</a> •
  <a href="#installation-and-configuration">Installation and configuration</a> •
  <a href="#how-to-use">How to use</a> •
  <a href="#notes-and-considerations">Notes and considerations</a> •
</p>

GIF

## How it Works  

The library **requests** is used to find a random article in Wikipedia. Then, the HTML content was obtained using **BeautifulSoup**, which as used to extract article title and first one hundread characters from summary (when it exist).

Next, a user interface was created using PySimpleGUI when the program asks the user if it would like to read some article from Wikipedia. If user clicks "Yes", the article link is open using webbrowser or a random article link is open if the user clicks "No". 


import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import PySimpleGUI as sg




In summary, we can divide the project into three stages:

1. Get data tweets through Tweepy API
2. Use TextBlob to detect polarity of text data
3. Create user interface using PySimpleGUI


## Installation and configuration 

### Clone this repository
```
git clone xxxxxx
```  
  
### Install development dependencies
```
pip install pandas  
pip install numpy  
pip install tweepy  
pip install -U textblob  
pip install PySimpleGUI  
pip install wordcloud  
pip install matplotlib
pip install PySimpleGUI
```  


## How to use

To start the interactive program open the python file **interactive_sentiment_analysis_twitter.py** in some IDE like VSCode, PyCharm and others.  

...or use terminal to run the program.  

![run_file](https://user-images.githubusercontent.com/44107852/215883432-40ab2c4c-7129-46c8-bf39-5f3dbe1da261.jpg)

Input your Twitter developer credentials and click Continue.

![input_credentials](https://user-images.githubusercontent.com/44107852/215883476-e17b19fc-e35e-421e-adeb-7c3cc1132787.jpg)

Input some keyword and click Search.

![window_search](https://user-images.githubusercontent.com/44107852/215883553-2d29cbaa-dbaa-473f-b2d5-76731cf0741f.jpg)

The three most recents tweets are showed.

Select a visualization and click Plot Visualization.

Pie chart
![pie_chart](https://user-images.githubusercontent.com/44107852/216157872-bb3f1ca0-754d-42e9-9307-4f184bf7518f.jpg)


Positives
![wordcloud_positives](https://user-images.githubusercontent.com/44107852/216157939-a693e962-e3d5-4224-b7c2-253bbcb48687.jpg)





## Notes and Considerations

At this point the TextBlob library works only to analysis in English. So....

During this development, I've learned how to use Dash and Plotly libraries, which was very challenging for me, in particular because of layout building and callbacks construction.





This is an apt project for those developers at the intermediary level looking to further their careers by developing creative and complex Python programs. 

which beginners can work on to put their Python knowledge to the test.

Developing real-world projects is the best way to hone your skills and materialize your theoretical knowledge into practical experience. 


You will need to acquaint yourself with new tools and technologies while working on a python project. The more you learn about cutting-edge development tools, environments, and libraries, the broader will be your scope for experimentation with your projects. 
