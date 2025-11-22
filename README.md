# House-Price-Prediction

## 1. Project Overview
This project is a Machine Learning application designed to estimate the market value of residential properties based on key features. It utilizes the **Linear Regression** algorithm to analyze historical housing data and predict prices based on user inputs. This project was built to demonstrate the practical application of data science concepts, including data loading, model training, and user interaction logic.

## 2. Features
The project includes the following functional modules:
* **Automated Data Management:** The system automatically loads training data from a CSV file. If the file is missing, it includes a self-correction module that generates a robust dataset automatically.
* **Machine Learning Model:** Implements `LinearRegression` from the *scikit-learn* library to learn the relationship between Area, BHK, Age, and Price.
* **Interactive Prediction:** A user-friendly command-line interface (CLI) where users can input property details to get real-time estimates.

## 3. Technologies Used
The following tools and libraries were used to build this project:
* **Python :** Core programming language.
* **IDLE :** Python text-editor.
* **Pandas:** For data manipulation and CSV file handling.
* **Scikit-Learn:** For implementing the Linear Regression machine learning algorithm.
* **OS:** For interacting with the computer's operating system.

## 4. Steps to Install & Run
Follow these instructions to set up the project on your local machine.
Ensure Python is installed on your system. You can check by running:
**python --version** in command prompt/terminal.
Download the code in your local storage
**Install Required Libraries:** Run the following command to install the necessary dependencies:
pip install pandas scikit-learn numpy
## Running the Project:
Execute the main script to start the application: **python main.py**

## 5. Instructions for Testing
* **Standard Input** : Enter 1500, 3, 5 $\rightarrow$ Expect a positive price (~85 Lakhs).
* **Edge Case:** Enter 600, 1, 30 $\rightarrow$ Expect a low positive price (no negative numbers).
* **Invalid Input:** Enter text (e.g., "Ten") $\rightarrow$ Expect "Input Error" message.
* **Negative Input:** Enter -500 $\rightarrow$ Expect "Positive values only" warning

## 6. Screenshots 

