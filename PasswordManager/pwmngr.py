from sys import argv, exit
import argparse
import csv
import cryptography


def main():
    help = (
        'usage: '
        + argv[0]
        + ' <options> [info]\n'
        + '-h, --help                                   Print Help Message and Exit'
        + '-n, --new [name email password]              Save New Password\n'
        + '-e, --edit [name email password]             Edit Existing Password\n'
        + '-d, --delete [name]                          Delete a Password\n'
        + '-f, --find [name]                            Find a Password\n'
        + '-l, --list                                   List All Passwords\n'
        + '-g, --generate *[-c <number>, -l, -u, -s]    Generate Random Password\n\n'
        + 'Or leave empty to enter The App'
    )

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
                genPW(argv[2], argv[3], argv[4])
            case '-h' | '--help':
                exit(help)
            case _:
                exit(help)
    except IndexError:
        run()


def run():
    options = '\nSave New Password: {n, new}\nEdit Existing Password: {e, edit}\nDelete a Password: {d, delete}\nFind a Password: {f, find}\nList All Password: {l, list}\nGenerate Random Password: {g, generate}\n: '

    while True:
        try:
            opr = input(options)
            match opr:
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
                        input('Chars: '),
                        input('Lowercase: l, Uppercase: u, RandomCase: r\n: '),
                        input('Include Symbols y/n: '),
                    )
                case _:
                    pass
        except (EOFError, KeyboardInterrupt):
            exit()


def newPW(name, email, pw):
    ...


def editPW(name, email, pw):
    ...


def delPW(name):
    ...


def findPW(name):
    ...


def listPW():
    ...


def genPW(charsNum, case, isSymbol):
    ...


if __name__ == '__main__':
    main()
