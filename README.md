## Novice Bodybuilding Program Generator

#### Description:

Desktop application designed to input a user's lifestyle characteristics along with their goals to create a personalized approach to bodybuilding. Aimed to be for beginners of all ages.

## Project Status

This project is currently in development. Users can input general data and recieve an output text file detailing simple workout routines designed to match their individuals. A simpler/cleaner functionality for program output is still in progress.

## Images

![First Input Page for Program](/gymproject/screenshots/P.P.1.png "First Input Page").

![Second Input Page for Program](/gymproject/screenshots/P.P.2.png "Second Input Page").

## Installation and Use

#### Installation:  

Clone down this repository. You will need `python` installed globally on your machine.  

#### Use:

Run the `main.py` file in the directory

Follow instructions inputting lifestyle, bodytype, and goals information until you see the "Generate" option.

Once the file has been generated, find the `program.txt` file in the same directory where the new workout routine has been output.


## Reflection

This was originally a side project built during the summer between my second and third year at Saint Louis University. The project's goals included using software design principles and other practices learned up until this point and refamiliarizing myself with Python for upcoming schoolwork/internship searches.

Originally I wanted to build an application to help beginner bodybuilders choose/create new workouts and routines designed to fit their lifestyles, bodytypes, and goals. I started this process with creating a UI using Python Tkinter as well as an open source customtkinter dependency to make the program feel more modern. Originally planning to use an exercise API, I decided a program designed for beginner would better benefit from a pre-defined set of workout logic rather than giving the user full control over their routines.

There weren't any roadblocks necessarily to this project, but its biggest challenges included learning the tkinter libraries as well as defining the backend logic. The project meant to cater towards beginners but of all ages and bodytypes, factoring in gender as well, so this developed complexities in the program (less free-weight use for older users, increased cardio for seniors and the general overweight, etc.)

Thus far, this project is still in progress. The main goal is satisfied, however, and the program is a working prototype. I intend to later develop another search tab using the original API, which included how to perform specific movements. Of what is currently built, the output system for the bodybuilding program needs to be improved (currently just outputs a .txt file).