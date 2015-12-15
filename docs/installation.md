# **Installation**
BlackEnd is currently designed to run on Python versions 2.9.0 and above.

Note :
These installation instructions are tested on Ubuntu 14.04 and Windows 10. Last verified on Windows 10 15/12/2015.

# **Overview**
This repository contains (primarily) Python code written on top of Django and other Python modules.

It should take you about 10 minutes to get the FutureMapper site running locally on your computer.

After running your own instance of the FutureMapper website, you can play with the code from an interactive shell on your computer.

# **Essentials**

### Open up a command prompt

Understanding how to open a command prompt for your operating system is an important prerequisite to master before continuing with the remaining installation instructions.

For the rest of these instructions, you have to open a command prompt:

* On a Linux or similar system, find a program with "terminal" or "console" in the name. Run it.
* On a Windows computer, you'll need to use Git Bash. To do so, download and install the .exe at this link. (It will ask you a bunch of questions. You can accept the defaults.) Once that is installed, launch Git Bash by going to: Start -> All Programs -> Git -> Git Bash

### Get the code from the GitHub repository
If you already have an blackend directory on your computer, then you already have the source code. You may skip to the next step.

If you're reading this installation instruction file on the web, then you will need to clone the repository from GitHub to your local computer.

* Create a virtual environment inside it by using the command : `virtualenv fmap`
* Navigate to virtual environment directory: `cd fmap`
* Activate virtual environment : `source bin/activate`
* On the command prompt, clone the blackend repository to your local computer : ` git clone https://github.com/FutureMapper/blackend.git`

### Install Requirements 
Before you run the commands in the this section, make sure you have changed your present working directory to the blackend directory.

In order to run the FutureMapper website, you have to install the requirements specified in the requirements.txt file first by running the command : `pip install -r requirements.txt`

### Set up the database
Your local FutureMapper site will store data in a SQLite database.

Run this command to create the database and add tables for our dependencies:

`python manage.py migrate`

`python manage.py loaddata sites`

### Run the site
Before you run the commands in the this section, make sure you have changed your present working directory to the blackend directory.

Run this command which will start a web server locally on your computer:

`python manage.py runserver`

As long as the "runserver" is running, you can visit your local version of the FutureMapper site in a web browser. So, try surfing to:

`http://localhost:8000/`

Your local version of FutureMapper does not contain any user data in its SQLite database. You may add users manually through the user interface.

