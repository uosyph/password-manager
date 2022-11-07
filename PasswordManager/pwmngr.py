from sys import argv, exit
import os
import base64
import csv
import pandas as pd
import secrets
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Color:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class Message:
    help = (
        f'{Color.BOLD}Usage:{Color.ENDC} {argv[0]} {Color.OKCYAN}[option]{Color.ENDC} {Color.OKGREEN}<info>{Color.ENDC}\n\n'
        + f'{Color.OKCYAN}-h{Color.ENDC}, {Color.OKCYAN}--help{Color.ENDC}                                   '
        + f'Print Help Message and Exit\n'
        + f'{Color.OKCYAN}-n{Color.ENDC}, {Color.OKCYAN}--new{Color.ENDC}       '
        + f'<{Color.OKGREEN}name email password{Color.ENDC}>        Save New Password\n'
        + f'{Color.OKCYAN}-e{Color.ENDC}, {Color.OKCYAN}--edit{Color.ENDC}      '
        + f'<{Color.OKGREEN}name email password{Color.ENDC}>        Edit Existing Password\n'
        + f'{Color.OKCYAN}-d{Color.ENDC}, {Color.OKCYAN}--delete{Color.ENDC}    '
        + f'<{Color.OKGREEN}name{Color.ENDC}>                       Delete a Password\n'
        + f'{Color.OKCYAN}-f{Color.ENDC}, {Color.OKCYAN}--find{Color.ENDC}      '
        + f'<{Color.OKGREEN}name{Color.ENDC}>                       Find a Password\n'
        + f'{Color.OKCYAN}-l{Color.ENDC}, {Color.OKCYAN}--list{Color.ENDC}                                   '
        + f'List All Passwords\n'
        + f'{Color.OKCYAN}-g{Color.ENDC}, {Color.OKCYAN}--generate{Color.ENDC}  '
        + f'<{Color.OKGREEN}number{Color.ENDC}>, [{Color.OKGREEN}-l{Color.ENDC}, '
        + f'{Color.OKGREEN}-u{Color.ENDC}, {Color.OKGREEN}-r{Color.ENDC}], {Color.OKGREEN}-s{Color.ENDC}   '
        + f'Generate Random Password\n\n'
        + f'{Color.BOLD}Or leave empty to enter The App.{Color.ENDC}'
    )

    options = (
        f'\nSave New Password:          [{Color.OKCYAN}n{Color.ENDC}, {Color.OKCYAN}new{Color.ENDC}]\n'
        + f'Edit Existing Password:     [{Color.OKCYAN}e{Color.ENDC}, {Color.OKCYAN}edit{Color.ENDC}]\n'
        + f'Delete a Password:          [{Color.OKCYAN}d{Color.ENDC}, {Color.OKCYAN}delete{Color.ENDC}]\n'
        + f'Find a Password:            [{Color.OKCYAN}f{Color.ENDC}, {Color.OKCYAN}find{Color.ENDC}]\n'
        + f'List All Password:          [{Color.OKCYAN}l{Color.ENDC}, {Color.OKCYAN}list{Color.ENDC}]\n'
        + f'Generate Random Password:   [{Color.OKCYAN}g{Color.ENDC}, {Color.OKCYAN}generate{Color.ENDC}]\n'
        + f'Quit The App:               [{Color.OKCYAN}q{Color.ENDC}, {Color.OKCYAN}quit{Color.ENDC}]\n'
        + f': '
    )


scrt = 'dr#y41rubi$woq-b_I+ru8run2wr-cE'
secret = scrt.encode()
salt = b'>b\xc9O\xf1\xd0\x95\x06\x9bs\x1a\xeb\x90B\xd7X'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend(),
)
key = base64.urlsafe_b64encode(kdf.derive(secret))

f = Fernet(key)


path = './'
filename = 'vault.csv'
filepath = path + filename


def main():
    check_file()
    get_arg()


def check_file():
    if not os.path.exists(filepath):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'email', 'password'])
            print('created file')


# Get user input from command line arguments
def get_arg():
    try:
        match argv[1].lower():
            case '-n' | '--new':
                newPW(argv[2].lower(), argv[3].lower(), argv[4])
            case '-e' | '--edit':
                editPW(argv[2].lower(), argv[3].lower(), argv[4])
            case '-d' | '--delete':
                delPW(argv[2].lower())
            case '-f' | '--find':
                findPW(argv[2].lower())
            case '-l' | '--list':
                listPW()
            case '-g' | '--generate':
                pwLen = 16
                case = 'r'
                useSymbols = 'y'

                try:
                    if argv[2] != None and int(argv[2]) > 0:
                        pwLen = argv[2]

                    match argv[3].lower():
                        case '-u' | '--uppercase':
                            case = 'u'
                        case '-l' | '--lowercase':
                            case = 'l'
                        case _:
                            case = 'r'

                    match argv[4].lower():
                        case '-s' | '--no-symbols':
                            useSymbols = 'n'
                        case _:
                            useSymbols = 'y'
                except IndexError:
                    pass

                genPW(int(pwLen), case, useSymbols)
            case '-h' | '--help':
                exit(Message.help)
            case _:
                exit(Message.help)
    except IndexError:
        run()


# Run the App in a terminal interface
def run():
    while True:
        try:
            option = input(Message.options).lower()
            match option:
                case 'n' | 'new':
                    newPW(
                        input(f'{Color.BOLD}Name: {Color.ENDC}').strip().lower(),
                        input(f'{Color.BOLD}Email: {Color.ENDC}').strip().lower(),
                        input(f'{Color.BOLD}Password: {Color.ENDC}').strip(),
                    )
                case 'e' | 'edit':
                    editPW(
                        input(f'{Color.BOLD}Name: {Color.ENDC}').strip().lower(),
                        input(f'{Color.BOLD}Email: {Color.ENDC}').strip().lower(),
                        input(f'{Color.BOLD}Password: {Color.ENDC}').strip(),
                    )
                case 'd' | 'delete':
                    delPW(input(f'{Color.BOLD}Name: {Color.ENDC}').strip().lower())
                case 'f' | 'find':
                    findPW(input(f'{Color.BOLD}Name: {Color.ENDC}').strip().lower())
                case 'l' | 'list':
                    listPW()
                case 'g' | 'generate':
                    while True:
                        try:
                            pwLen = int(
                                input(
                                    f'{Color.BOLD}Password Length: {Color.ENDC}'
                                ).strip()
                            )

                            case = (
                                input(
                                    f'{Color.BOLD}Lowercase: l, Uppercase: u, RandomCase: r\n: {Color.ENDC}'
                                )
                                .strip()
                                .lower()
                            )
                            if case not in ['l', 'u', 'r']:
                                raise ValueError

                            use_symbols = (
                                input(f'{Color.BOLD}Include Symbols y/n: {Color.ENDC}')
                                .strip()
                                .lower()
                            )
                            if use_symbols not in ['y', 'n']:
                                raise ValueError

                            break
                        except ValueError:
                            print(f'{Color.FAIL}Wrong Option.{Color.ENDC}\n')
                            pass

                    genPW(pwLen, case, use_symbols)
                case 'q' | 'quit':
                    exit()
                case _:
                    print(f'{Color.FAIL}Wrong Option.{Color.ENDC}\n')
                    pass
        except ValueError:
            print(f'{Color.FAIL}Wrong Value.{Color.ENDC}\n')
            pass
        except (EOFError, KeyboardInterrupt):
            exit()


# encryption function
def encrypt(str):
    str = str.encode()
    return (f.encrypt(str)).decode()


# decryption function
def decrypt(str):
    str = str.encode()
    return (f.decrypt(str)).decode()


# Add a new password to the vault, and encrypt the password before saving
def newPW(name, email, password):
    password = encrypt(password)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        try:
            writer.writerow([name, email, password])
            print(f'{Color.OKGREEN}Password Saved Successfully{Color.ENDC}')
            return
        except csv.Error as e:
            print(f'{Color.FAIL}Unable to Save Password{Color.ENDC}')
            exit('file {}, line {}: {}'.format(filename, writer, e))


# Edit a password in the vault using the name associated with it, and encrypt the new password before saving
def editPW(name, email, password):
    password = encrypt(password)
    with open(filename, newline='') as rFile, open(filename, 'a', newline='') as wFile:
        reader = csv.reader(rFile)
        writer = csv.writer(wFile)
        try:
            for row in reader:
                if row[0] == name:
                    row[1] = row[1].replace(row[1], email)
                    row[2] = row[2].replace(row[2], password)

                    file = pd.read_csv(filename)
                    file.drop(file.index[(file["name"] == name)], axis=0, inplace=True)
                    file.to_csv(filename, index=False)

                    writer.writerow(row)

                    print(f'{Color.OKGREEN}Password Edited Successfully{Color.ENDC}')
                    return
        except csv.Error as e:
            exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        print(f'{Color.FAIL}Unable to Find Password{Color.ENDC}')


# Delete a password in the vault using the name associated with it
def delPW(name):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        try:
            for row in reader:
                if row[0] == name:
                    file = pd.read_csv(filename)
                    file.drop(file.index[(file["name"] == name)], axis=0, inplace=True)
                    file.to_csv(filename, index=False)

                    print(f'{Color.OKGREEN}Password Deleted Successfully{Color.ENDC}')
                    return
            print(f'{Color.FAIL}Unable to Find Password{Color.ENDC}')
        except csv.Error as e:
            exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


# Find a password in the vault using the name associated with it, and decrypt the password before displaying
def findPW(name):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            row[2] = decrypt(row[2])
            if row[0] == name:
                print(
                    f'{Color.BOLD}Name: {Color.ENDC}{Color.OKBLUE}{row[0]}{Color.ENDC}\t{Color.BOLD}Email: {Color.ENDC}{Color.OKBLUE}{row[1]}\t{Color.ENDC}{Color.BOLD}Password: {Color.ENDC}{Color.OKBLUE}{row[2]}{Color.ENDC}',
                    end='\n',
                )
                return
        print(f'{Color.FAIL}Unable to Find Password{Color.ENDC}')


# List all password in the vault, and decrypt the passwords before displaying
def listPW():
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            row[2] = decrypt(row[2])
            print(
                f'{Color.BOLD}Name: {Color.ENDC}{Color.OKBLUE}{row[0]}{Color.ENDC}\t{Color.BOLD}Email: {Color.ENDC}{Color.OKBLUE}{row[1]}\t{Color.ENDC}{Color.BOLD}Password: {Color.ENDC}{Color.OKBLUE}{row[2]}{Color.ENDC}',
                end='\n',
            )
        return


# Password generator, user can deferment the length, lower or upper or mixed case, and to use special characters (symbols) or not
def genPW(pwLen, case='r', useSymbols='y'):
    letters = string.ascii_letters
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    alpha = ''
    pw = ''

    if pwLen != None and pwLen > 0:
        pw_length = pwLen
    else:
        pw_length = 16

    match case:
        case '-u' | '--uppercase' | 'u' | 'uppercase':
            alpha = upper_letters + digits
        case '-l' | '--lowercase' | 'l' | 'lowercase':
            alpha = lower_letters + digits
        case _:
            alpha = letters + digits

    match useSymbols:
        case '-s' | '--symbols' | 'y':
            alpha = alpha + special_chars

    for _ in range(pw_length):
        pw += ''.join(secrets.choice(alpha))

    print(f'\n{Color.OKGREEN}{pw}{Color.ENDC}')


if __name__ == '__main__':
    main()
