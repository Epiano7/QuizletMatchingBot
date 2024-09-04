# Quizlet Matching Bot

A brute-force botting service for Quizlet's Matching game mode.

# Dependencies:
Requires NordVPN (used to attempt to bypass bot detection)


# Install
Create a project in your IDLE (I'd recommend PyCharm) and copy over the
main.py file to the project. Run it and
it will require you to input any letter to start the program.
If you want to stop it, hit Control+Alt+Delete and move your mouse
to a corner of the screen, then close out of the menu.



# Config
The code is set up for a 1440p monitor so you might need to change
the cooridanate points to where they are on your screen.
Under the function Click() there is a list of coordinates. Use pyautogui.position()
(after moving the mouse to the matching card) to find the x and y of it, then replace
the coordinate pair with the one you made.

# Issues
If you find any bugs (hopefully not) or improvements you can make a pull request and
I'll take a look at it.
