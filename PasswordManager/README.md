# Password Manager

## Video Demo: []()

## Description:

A password manager that lets the user store, edit, delete, find, and list the passwords they have.
Passwords are encrypted before being saved to a CSV file and decrypted before being displayed to the user.
Users can generate a random password and determine its length, whether to use symbols or not, and whether to use uppercase, lowercase, or mixed-case.

---

## Directory Contents:
- **project.py**: This is the file which contains The `main` function and the other functions and classes necessary to implement the App.
- **test_project.py**: This file contains the test functions for `project.py`.
- **requirements.txt**: All `pip`-installable libraries that are used in the project are listed here.


## Getting Started:
### Basics:

Get the app:
```
git clone https://github.com/yousafesaeed/python-scripts.git && cd python-scripts/PasswordManager/
```

Install the dependencies:

Note: `pytest` is optional if you don't care about tests.

```
pip install -r requirements.txt
```

or

```
pip install cryptography pandas pytest
```

### Usage:

Run the app in the terminal:
```
python pwmngr.py
```

Use it with command line arguments:
```
python pwmngr.py [argument] <information>
```
Note: If multiple pieces of information are requested, you must enter them all in the same order, separated by a space.

Available arguments:

`-n` or `--new` : save a new password. (*requires three arguments: name email password*)

`-e` or `--edit` : edit an existing password. (*requires three arguments: name email password*)

`-d` or `--delete` : delete a password. (*requires one arguments: name*)

`-f` or `--find` : find a password. (*requires one arguments: name*)

`-l` or `--list` : list all password. (*requires no arguments*)

`-g` or `--generate` : generate a random password. (*can use three optional arguments: length case symbols*)

- `length`: the length of the password (*must be an integer*) (*or don't include the argument to use the default length*) **default is 16**
- `case`: which case to use in the password [*`-l` for lower-case*] [*`-u` for upper-case*] (*or don't include the argument for mixed-case*) **default is mixed-case**
- `symbols`: use symbols or not in the password [*`-s` or `--no-symbols` to not include symbols*] (*or don't include the argument to include symbols*) **default is include symbols**

`-h` or `--help` : print help message.


## Libraries Used:
Note: These libraries can be used in a wide variety of ways. I mentioned just what I used them for in this project.

### Third-party:
- **cryptography**: for password encryption.
- **pandas**: for manipulating CSV files, e.g., editing and deleting rows.
- **pytest**: for testing the app and its functions.

### Standard:
- **base64**: used with `cryptography` to generate a key.
- **sys**: getting arguments and exiting the app.
- **os**: checking the existence of files and simulating user input.
- **io**: getting output from the console.
- **string**: getting upper- and lower-case letters, numbers, and special characters (symbols).
- **secrets**: genreting a random string based on a specified length and set of characters.
- **csv**: reading and writing from and to CSV files.










## Documentation:

### *project.py* Functions (excluding main):

#### Function:

***check_file()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***encrypt()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***decrypt()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***get_arg()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***run()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***newPW()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***editPW()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***delPW()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***findPW()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***listPW()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 


#### Function:

***genPW()***

#### Description:

- 

#### Arguments:

- 

#### Side effects:

- 

#### Returns:

- 



### *test_project.py* Functions:

Each function in `project.py` has its own test function in `test_project.py` to test it in a variety of ways and scenarios to make sure it's working the way it's intended to be used, and in case anything goes wrong in terms of usage by the user. It's also capable of catching it and taking the proper action.










<!--
    title: CS50P Final Project - Password Manager
    desc:  My final project for Harvard's CS50P - Password Manager

    A password manager that lets the user store, edit, delete, find, and list the passwords they have.
    Passwords are encrypted before being saved to a CSV file and decrypted before being displayed to the user.
    Users can generate a random password and determine its length, whether to use symbols or not, and whether to use uppercase, lowercase, or mixed case.

    Project details and source code: https://github.com/yousafesaeed/python-scripts/tree/main/PasswordManager 
    Timestamps: 
    Intro - 00:00
    
    Tests - 00:00
-->