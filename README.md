# Endless Arithmetic Quiz

This is basic a quiz that runs in terminal. You will be asked an endless stream of basic arithmetic questions until you get one wrong. At the end you'll see how many you got right.

## Requirements

•	Python 3 (version 3.9 or higher)
•	No additional libraries are needed — the quiz uses only Python's built-in modules

## How to Download the Quiz

1.	Go to the GitHub repository link provided
2.	Click the green Code button, then click Download ZIP
3.	Unzip the folder to a location you can find easily (e.g. your Desktop)


## How to Run the Quiz

1.	Open a terminal (on Windows: Command Prompt or PowerShell; on Mac/Linux: Terminal)
2.	Navigate to the folder where the quiz files are saved. For example:

```shell
cd Desktop/formative_quiz
```

3.	Run the quiz by typing:

```shell
main.py
```

4.	Follow the on-screen instructions to answer the questions


## How to Play

When the quiz starts, you will be asked a question. Begin by typing in your answer (answers will always be numerical) and continue until you get one wrong.


# Technical Documentation

## Project Structure

The project is made up of the following files:

	- main.py - the main file that runs the quiz
	- generate_questions.py - stores the questions and answers
	- README.md - this documentation file

## How the Code Works

The program is split into two modules to keep the code clean and easy to read.

## generate_questions.py

This file contains the questions, this uses the random library that is imported in, it then generates two random numbers from 1-15 and randomly picks whether to carry out additions, substraction or multiplication. It will then determine the answer.

## main.py

This file is the entry point of the program. It imports the questions from generate_questions.py. It then runs the main quiz loop, checking the answer is correct, keeping a running score and then displays the final score at the end.

## How to Run the Code (for Developers)

Make sure Python 3 is installed, then from the project directory run:

    main.py

No third-party packages are required. The program uses only the following standard library modules:

•	random — used to shuffle the order of questions each time the quiz runs

## GitHub Repository

The source code for this project is hosted on GitHub. The repository includes all .py files, this README, and version history.

Repository URL: https://github.com/dan54borg/formative_quiz.git

To clone the repository:

```bash
git clone https://github.com/dan54borg/formative_quiz.git
```

## How to Edit Questions

The only variable to edit for the questions is to increase or decrease the range of the randomly selected number.
In the file generate_questions.py on line 5 and 6 (see code block below)

```python
    num_1 = random.randint(1,15)    
    num_2 = random.randint(1,15) 
```

Edit the numbers within the brackets, with the first value being the starting point and the second value the end of the range.

