from sys import argv, exit
import argparse
import csv
import cryptography


def main():
    print_help = print(
        'usage: '
        + argv[0]
        + ' [options] <info>\n'
        + '-n, --new         Save New Password\n'
        + '-e, --edit        Edit Existing Password\n'
        + '-d, --delete      Delete a Password\n'
        + '-f, --find        Find a Password\n'
        + '-l, --list        List All Passwords\n'
        + '-g, --generate *[-c <number>, -l, -u, -s]    Generate Random Password\n'
    )

    try:
        match argv[1]:
            case '-n' | '--new':
                print('new acc')
            case '-e' | '--edit':
                print('')
            case '-d' | '--delete':
                print('')
            case '-f' | '--find':
                print('')
            case '-l' | '--list':
                print('')
            case '-g' | '--generate':
                print('')
            case _:
                print_help

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


def listPW(force):
    ...


def genPW(charsNum, case, isSymbol):
    ...


def running():
    ...


if __name__ == '__main__':
    main()
