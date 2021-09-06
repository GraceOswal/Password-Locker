# Password-Locker

## Author

Grace Osswal

## Description

This project is built up using python language. The application [Password Locker] helps the user to signup,login,delete and also copy his/her credentials
inside the app.

## Screenshot

<img src="https://github.com/GraceOswal/Password-Locker/blob/master/images/passlocker.png">

## User Objectives

* The user creates an account for the application(signup) or logs' into(login) to the application.
* The user can also store the existing accounts details for various accounts that he/she has registered in..
* ...Generates new password for an account that have not been registered for and stored into the account.
* The user can also delete stored account details .
* Credentials can also be copied in the clipboard.

## Installation / Setup instruction

## The application requires the following installations to operate

* python3.8
* pyperclip
* pip3

## Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/GraceOswal/Password-Locker.git```

* cd Password-Locker

* code the project with your preferred text editor.

### Run Application

* To run the application, open the cloned file in terminal and run the following commands:

        chmod +x pwd.py
        ./pwd.py
* To run test for the application
        $ python3 passlock_test.py

## Behaviour Driven Development

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./pwd.py```|...Welcome to Password Locker... *CA ---  Create New Account* LI ---  Get An Account |
|Select  CA| input username and password| Hello ```username```, Hooray! Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password...choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```Del```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|

## Technologies Used

* python3.8

## Known Bugs

* No confirmed bugs

## Contact Information

If you have any question or contributions, please email me at [grace.osswal@student.moringaschool.com]

## License

* *MIT License:*
* Copyright (c) 2021 **Oswal Grace**
