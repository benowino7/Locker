# LOCKER

This project was generated with ```Python3.6.```

## Installation

* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Run ```python3.6 run.py``` code in the terminal to launch.

## Usage

* launch and you can either create a new user, or login or exit the application.
* If you choose option ```(l),``` use: ```testuser``` as username and ```345678``` as PassWord
* If you choose to create a new account, use  option```c``` as the code and follow the prompts.
* you can:
```
     View Your saved credentials, Add new credentials, Remove credentials, Search credentials or Log Out.

```
if you log in
* use option```(x)``` to exit
## Running unit tests

* Run ```python3.6 credentials_test.py``` >>> credential  tests.
* Run ```python3.6 test_user.py``` >>> user  tests.

## Bugs.

Since there is no database to support the app, once you exit or log out of a session you loose all the credentials and created user. You have to create a new user for every session.
You can still use the default login but if you exit the app, you will still loose all the credentials you created.
## BBD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./list.py** | Hi there, Welcome to the Password vault, What do we call you? |
| Display prompt for creating an account | **Enter: c** | Enter your first name, last name, password and email address |
| Display prompt for login in | **Enter: l** | Enter your account details to log in |
| Display codes for navigation | **Successful login** | Choose an option: c - Create Credential, dis - Display Credentials, cp - Copy Credential, go - exit |
| Display prompt for creating a credential | **Enter: c** | Enter the site name, credentials, password and email address |
| Display a list of credentials | **Enter: d** | Prints a list of saved credentials |
| Exit application | **Enter: x** | Exit the current navigation stage |
```
 the project will require the user to enter username and generate or create his/her password
 view credentials and add 
 exit if finished
 ```

 ## Contributing

```
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
firs fork , git clone the cloned repo to your machine, contribute the pull request back to the repository.
```

## Further help
For additions, submit a pull request and you can make contributions at will.
Alternatively reach me through: ```bensonowino7@gmail.com```

## License

MIT License(https://choosealicense.com/licenses/mit/)
