
# Cookie Clicker automation
[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in%20VSCode-blue?logo=visualstudiocode)](https://vscode.dev/github/username/repo) 

Project to create a bot using selenium to play the Cookie Clicker game. The project consist in automate the clicking in the Big Cookie, buy products and upgrades to increase productivity. 




## Authors

- [@henriqueborgo](https://www.github.com/henriqueborgo)


## Introduction

This project uses the Selenium library to locate and interact with HTML elements in the interface of the game. The script will open a new tab browser tab, accept the cookies settings and select English as language of the game. After that, it will wait 5 seconds to the game to properly load and then start interacting with the game elements. To increase productivity, the game will run in different thread the clicking the big cookie and the loop to buy products and upgrades.











## Summary of Tech Stack

This project was built using **Python**.
To run this project import libraries:

- threading
- time
- selenium


    



## Running Locally

Running the Log project in your local dev environment is very easy. Be sure to have Python installed, then follow the directions bellow.

1. Clone the source code.

2. Be sure that your browser is updated and then dowload the correspondent WebDrivrer to the same folder as the respository. For this project it was used the ChromeDriver, which you can download here: https://sites.google.com/chromium.org/driver/ 

3. Run main.py


## Demonstration
![Running Demonstration](images/cookie_clicker_demonstration.gif)
