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

The HTTP library **requests** was used to find a random article on Wikipedia. Then, the HTML content was obtained using **BeautifulSoup**, which was also used to extract the title of the article and the first hundred characters of the abstract (if any).
Afterwards, a user interface was created using **PySimpleGUI**. The program asks the user if he would like to read any Wikipedia articles and presents its title and summary. If the user clicks "Yes", the article link will be opened using **webbrowser** module or a random article link will be opened if the user clicks "No".

In summary, we can divide the project into three stages:

1. Get random article from Wikipedia
2. Use BeautifulSoup to extract article title and abstract
3. Create user interface using PySimpleGUI


## Installation and configuration 

### Clone this repository
```
git clone https://github.com/GiovannaBezerra/random_wikipedia_article.git
```  
  
### Install development dependencies
```
requests
beautifulsoup4
webbrowser
PySimpleGUI
```  


## How to use

After cloning the repository, to start the interactive program open the python file [random_wikipedia_article.py](https://github.com/GiovannaBezerra/random_wikipedia_article/blob/main/random_wikipedia_article.py) in some IDE like VSCode, PyCharm and others.  

...or use terminal to run the program.  

run-file

The program opens the window with some wikipedia article read suggestion.
read_suggestion_yes

If the user clicks "Yes", the link is open:
article1


Or some random article if the user clicks "No":

read_suggestion_no


## Notes and Considerations

At this point the TextBlob library works only to analysis in English. So....

During this development, I've learned how to use Dash and Plotly libraries, which was very challenging for me, in particular because of layout building and callbacks construction.





This is an apt project for those developers at the intermediary level looking to further their careers by developing creative and complex Python programs. 

which beginners can work on to put their Python knowledge to the test.

Developing real-world projects is the best way to hone your skills and materialize your theoretical knowledge into practical experience. 


You will need to acquaint yourself with new tools and technologies while working on a python project. The more you learn about cutting-edge development tools, environments, and libraries, the broader will be your scope for experimentation with your projects. 
