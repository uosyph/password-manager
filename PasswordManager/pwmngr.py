from sys import argv, exit
import csv
import argparse
import cryptography
import secrets
import string


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Message:
    help = (
        f'usage: {argv[0]} <options> [info]\n'
        + '-h, --help                                   Print Help Message and Exit\n'
        + '-n, --new [name email password]              Save New Password\n'
        + '-e, --edit [name email password]             Edit Existing Password\n'
        + '-d, --delete [name]                          Delete a Password\n'
        + '-f, --find [name]                            Find a Password\n'
        + '-l, --list                                   List All Passwords\n'
        + '-g, --generate *[-c <number>, -l, -u, -s]    Generate Random Password\n\n'
        + 'Or leave empty to enter The App'
    )
    options = '\nSave New Password: {n, new}\nEdit Existing Password: {e, edit}\nDelete a Password: {d, delete}\nFind a Password: {f, find}\nList All Password: {l, list}\nGenerate Random Password: {g, generate}\n: '


filename = 'vault.csv'


def main():
    get_arg()


def get_arg():
    try:
        match argv[1]:
            case '-n' | '--new':
                newPW(argv[2], argv[3], argv[4])
            case '-e' | '--edit':
                editPW(argv[2], argv[3], argv[4])
            case '-d' | '--delete':
                delPW(argv[2])
            case '-f' | '--find':
                findPW(argv[2])
            case '-l' | '--list':
                listPW()
            case '-g' | '--generate':
                genPW(int(argv[2]), argv[3], argv[4])
            case '-h' | '--help':
                exit(Message.help)
            case _:
                exit(Message.help)
    except IndexError:
        run()


def run():
    while True:
        try:
            option = input(Message.options)
            match option:
                case 'n' | 'new':
                    newPW(input('Name: '), input('Email: '), input('Password: '))
                case 'e' | 'edit':
                    editPW(input('Name: '), input('Email: '), input('Password: '))
                case 'd' | 'delete':
                    delPW(input('Name: '))
                case 'f' | 'find':
                    findPW(input('Name: '))
                case 'l' | 'list':
                    listPW()
                case 'g' | 'generate':
                    genPW(
                        int(input('Password Length: ')),
                        input('Lowercase: l, Uppercase: u, RandomCase: r\n: '),
                        input('Include Symbols y/n: '),
                    )
                case _:
                    print('Wrong Option')
                    pass
        except (EOFError, KeyboardInterrupt):
            exit()
        except ValueError:
            print('Wrong Value')
            pass


def newPW(name, email, password):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        try:
            writer.writerow([name, email, password])
            print(f'{Color.OKGREEN}Password Saved Successfully{Color.ENDC}')
        except csv.Error as e:
            exit('file {}, line {}: {}'.format(filename, writer, e))
        except (EOFError, KeyboardInterrupt):
            exit()


def editPW(name, email, password):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        try:
            for row in reader:
                if row[0] == name:
                    row[1] = row[1].replace(row[1], email)
                    row[2] = row[2].replace(row[2], password)

                    print(row[0], '\n', row[1], '\n', row[2], '\n', row)
                    # with open(filename, 'a', newline='') as file:
                    #     writer = csv.writer(file)
                    #     writer.writerow(row)
                    #     time.sleep(1)
        except csv.Error as e:
            exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        except (EOFError, KeyboardInterrupt):
            exit()


def delPW(name):
    with open(filename, newline='') as inFile, open(
        filename, 'a', newline=''
    ) as outFile:
        reader = csv.reader(inFile)
        writer = csv.writer(outFile)
        for row in reader:
            if row[0] == name:
                ...


def findPW(name):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                print(
                    f'{Color.BOLD}Name: {Color.ENDC}{Color.OKBLUE}{row[0]}{Color.ENDC}\t{Color.BOLD}Email: {Color.ENDC}{Color.OKBLUE}{row[1]}\t{Color.ENDC}{Color.BOLD}Password: {Color.ENDC}{Color.OKBLUE}{row[2]}{Color.ENDC}',
                    end='\n',
                )


def listPW():
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(
                f'{Color.BOLD}Name: {Color.ENDC}{Color.OKBLUE}{row[0]}{Color.ENDC}\t{Color.BOLD}Email: {Color.ENDC}{Color.OKBLUE}{row[1]}\t{Color.ENDC}{Color.BOLD}Password: {Color.ENDC}{Color.OKBLUE}{row[2]}{Color.ENDC}',
                end='\n',
            )


def genPW(pwLen=None, case=None, useSymbol=None):
    letters = string.ascii_letters
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    alpha = ''
    pwd = ''

    # use argparser

    match case:
        case '-u' | '--uppercase':
            alpha = upper_letters + digits + special_chars
        case '-l' | '--lowercase':
            alpha = lower_letters + digits + special_chars
        case _:
            alpha = letters + digits + special_chars

    match useSymbol:
        case '-s' | '--symbols':
            alpha = letters + digits
        case _:
            alpha = letters + digits + special_chars


    
    if pwLen == None:
        pwd_length = 16
    else:
        pwd_length = pwLen


    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alpha))

    print(pwd)


if __name__ == '__main__':
    main()
