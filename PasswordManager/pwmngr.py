from sys import argv, exit
import csv
import argparse
import cryptography
import secrets
import string


# Add a proper way to exit the app
# Check if args when using -g flag either by using argparse or if cond
# Fix exit and delete funcs


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
        f'Usage: {argv[0]} [option] <info>\n\n'
        + '-h, --help                                   Print Help Message and Exit\n'
        + '-n, --new     <name email password>          Save New Password\n'
        + '-e, --edit    <name email password>          Edit Existing Password\n'
        + '-d, --delete  <name>                         Delete a Password\n'
        + '-f, --find    <name>                         Find a Password\n'
        + '-l, --list                                   List All Passwords\n'
        + '-g, --generate *[<number>, [-l, -u], -s]     Generate Random Password\n\n'
        + 'Or leave empty to enter The App'
    )

    options = (
        'Save New Password: [n, new]\n'
        + 'Edit Existing Password: [e, edit]\n'
        + 'Delete a Password: [d, delete]\n'
        + 'Find a Password: [f, find]\n'
        + 'List All Password: [l, list]\n'
        + 'Generate Random Password: [g, generate]\n: '
    )


filename = 'vault.csv'


def main():
    get_arg()


# Get user input from command line arguments
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


# Run the App in a terminal interface
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
                    while True:
                        try:
                            pwLen = int(input('Password Length: '))

                            case = input(
                                'Lowercase: l, Uppercase: u, RandomCase: r\n: '
                            )
                            if case not in ['l', 'u', 'r']:
                                raise ValueError

                            use_symbols = input('Include Symbols y/n: ')
                            if use_symbols not in ['y', 'n']:
                                raise ValueError

                            break
                        except ValueError:
                            print(f'{Color.FAIL}Wrong Option.{Color.ENDC}\n')
                            pass

                    genPW(pwLen, case, use_symbols)
                case _:
                    print(f'{Color.FAIL}Wrong Option.{Color.ENDC}\n')
                    pass
        except ValueError:
            print(f'{Color.FAIL}Wrong Value.{Color.ENDC}\n')
            pass
        except (EOFError, KeyboardInterrupt):
            exit()


# Add a new password to the vault
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


# Edit a password in the vault using the name associated with it
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


# Delete a password in the vault using the name associated with it
def delPW(name):
    with open(filename, newline='') as inFile, open(
        filename, 'a', newline=''
    ) as outFile:
        reader = csv.reader(inFile)
        writer = csv.writer(outFile)
        for row in reader:
            if row[0] == name:
                ...


# Find a password in the vault using the name associated with it
def findPW(name):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                print(
                    f'{Color.BOLD}Name: {Color.ENDC}{Color.OKBLUE}{row[0]}{Color.ENDC}\t{Color.BOLD}Email: {Color.ENDC}{Color.OKBLUE}{row[1]}\t{Color.ENDC}{Color.BOLD}Password: {Color.ENDC}{Color.OKBLUE}{row[2]}{Color.ENDC}',
                    end='\n',
                )


# List all password in the vault
def listPW():
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(
                f'{Color.BOLD}Name: {Color.ENDC}{Color.OKBLUE}{row[0]}{Color.ENDC}\t{Color.BOLD}Email: {Color.ENDC}{Color.OKBLUE}{row[1]}\t{Color.ENDC}{Color.BOLD}Password: {Color.ENDC}{Color.OKBLUE}{row[2]}{Color.ENDC}',
                end='\n',
            )


# Password generator, user can deferment the length, lower or upper or random case, and to use special characters (symbols) or not
def genPW(pwLen, case='r', useSymbol='y'):
    letters = string.ascii_letters
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    alpha = ''
    pw = ''

    if pwLen != None:
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

    match useSymbol:
        case '-s' | '--symbols' | 'y':
            alpha = alpha + special_chars

    for i in range(pw_length):
        pw += ''.join(secrets.choice(alpha))

    print(f'\n{Color.OKGREEN}{pw}{Color.ENDC}\n')


if __name__ == '__main__':
    main()
