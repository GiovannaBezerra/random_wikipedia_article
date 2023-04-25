<img src="https://user-images.githubusercontent.com/44107852/234053564-e2fda92f-5f46-44d7-b9b4-956ae824adb9.png" align="right"
      width="80" height="80">
      
# RANDOM WIKIPEDIA ARTICLE

This program searches Wikipedia and fetches a random article. Then it asks the user if he wants to read that article or not. If the answer is yes, the material is shown; otherwise, another random report is presented.

The aim of this project is to develop new python skills and materialize theoretical knowledge into practical experience.

<p align="center">
  <a href="#how-it-works">How it works</a> •
  <a href="#installation-and-configuration">Installation and configuration</a> •
  <a href="#how-to-use">How to use</a> •
  <a href="#notes-and-considerations">Notes and considerations</a> •
</p>

![gif](https://user-images.githubusercontent.com/44107852/234350913-32905da6-1ef0-4ada-b288-389e2fe0654d.gif)

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

![run-file](https://user-images.githubusercontent.com/44107852/234305069-6348f53f-d7b2-4b1b-9f6e-7da2d892571f.jpg)

The program opens the window with some Wikipedia article read suggestion.

![read_suggestion_yes](https://user-images.githubusercontent.com/44107852/234305184-a95d82da-da3d-458b-8225-9c2074238645.jpg)

If the user clicks "Yes", the indicated article link will be opened:

![article1](https://user-images.githubusercontent.com/44107852/234305278-f577ef90-005c-44e6-b66d-7fdb6dc5d659.jpg)

Or some random article will open if the user clicks "No":

![read_suggestion_no](https://user-images.githubusercontent.com/44107852/234305366-4f53730e-ca36-4502-bb77-988022ab451b.jpg)


## Notes and Considerations

During this development, I had the opportunity to improve my Python Skills and learn more about PySimpleGUI as a user interface. 
That way, I was able to acquaint myself with new tools, technologies, environments, and libraries while working on a real-world project.
