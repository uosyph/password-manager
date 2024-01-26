# Password Manager

## Description:

A password manager that lets the user store, edit, delete, find, and list the passwords they have.
Passwords are encrypted before being saved to a CSV file and decrypted before being displayed to the user.
Users can generate a random password and determine its length, whether to use symbols or not, and whether to use uppercase, lowercase, or mixed-case.

---

## Directory Contents:
- **pmngr.py**: This is the file which contains The `main` function and the other functions and classes necessary to implement the App.
- **test_pmngr.py**: This file contains the test functions for `pmngr.py`.
- **requirements.txt**: All `pip`-installable libraries that are used in the project are listed here.


## Getting Started:
### Basics:

Get the app:
```
git clone https://github.com/uosyph/password-manager.git && cd password-manager
```

Install the dependencies:

```
pip install -r requirements.txt
```

or

Note: `pytest` is optional if you don't care about tests.

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

### *pmngr.py* Functions (excluding main):

#### Function:

```python
check_file()
```

#### Description:

- Checks to see if `vault.csv` exists; if not, it is created and the first record is saved as (**name**,**email**,**password**).

#### Arguments:

- Doesn't take any arguments.

#### Side effects:

- Creates `vault.csv` and saves the first record as (**name**,**email**,**password**).

#### Returns:

- Doesn't return any value.


#### Function:

```python
get_arg()
```

#### Description:

- Gets command-line arguments and determines which function should be run.

#### Arguments:

- Doesn't take any arguments.

#### Side effects:

- Runs the proper function, runs the app, or exits the app.

#### Returns:

- Doesn't return any value.


#### Function:

```python
run()
```

#### Description:

- An infinite loop to get user input and execute the proper function.

#### Arguments:

- Doesn't take any arguments.

#### Side effects:

- Encourages the user to input a command or piece of information, then passes it to the proper function.

#### Returns:

- Doesn't return any value.


#### Function:

```python
encrypt()
```

#### Description:

- Encode the string, then encrypt it, then decode it and return it.

#### Arguments:

- `str`: any length string.

#### Side effects:

- There are no side effects.

#### Returns:

- The encrypted and decoded string.


#### Function:

```python
decrypt()
```

#### Description:

- Encode the encrypted string, then decrypt it, then decode it and return it.

#### Arguments:

- `str`: encrypted string.

#### Side effects:

- There are no side effects.

#### Returns:

- The decrypted and decoded string.


#### Function:

```python
newPW()
```

#### Description:

- Creates a new encrypted password and saves it to `vault.csv`.

#### Arguments:

- `name`: the name of the service/website
- `email`: the email used in the service/website
- `password`: the password used in the service/website

#### Side effects:

- encrypt the password.
- open the csv file and write to it the name, email, and password.
- prints status.

#### Returns:

- Doesn't return any value.


#### Function:

```python
editPW()
```

#### Description:

- Edits an already existing password in `vault.csv`.

#### Arguments:

- `name`: the name of the service/website you want to edit.
- `email`: the new email.
- `password`: the new password. 

#### Side effects:

- encrypt the new password.
- Open the csv file and delete the old password, then add the new name, email, and password.
- prints status.

#### Returns:

- Doesn't return any value.


#### Function:

```python
delPW()
```

#### Description:

- Deletes a password in `vault.csv`.

#### Arguments:

- `name`: the name of the service/website.

#### Side effects:

- open the csv file and delete the password from it.
- prints status.

#### Returns:

- Doesn't return any value.


#### Function:

```python
findPW()
```

#### Description:

- find a password in `vault.csv`.

#### Arguments:

- `name`: the name of the service/website.

#### Side effects:

- print the name, email, and password in an easy-to-read way.
- print status if it doesn't exist.

#### Returns:

- Doesn't return any value.


#### Function:

```python
listPW()
```

#### Description:

- list all password in `vault.csv`.

#### Arguments:

- Doesn't take any arguments.

#### Side effects:

- print the all names, emails, and passwords in an easy-to-read way.
- print status if there is no password saved.

#### Returns:

- Doesn't return any value.


#### Function:

```python
genPW()
```

#### Description:

- Generate a random password where users can determine its length, whether to use symbols or not, and whether to use uppercase, lowercase, or mixed-case.

#### Arguments:

- `pwLen`: the length of tha password **default is 16**
- `case`: which case to use **default is mixed-case**
- `useSymbols`: whether to use symbols or not **default is yes**

#### Side effects:

- prints the generate password.

#### Returns:

- Doesn't return any value.


### *test_pmngr.py* Functions:

Each function in `pmngr.py` has its own test function in `test_pmngr.py` to test it in a variety of ways and scenarios to make sure it's working the way it's intended to be used, and in case anything goes wrong in terms of usage by the user. It's also capable of catching it and taking the proper action.

