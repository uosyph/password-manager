import pytest
import os
import csv
import io
import sys
from pmngr import (
    check_file,
    get_arg,
    run,
    encrypt,
    decrypt,
    newPW,
    editPW,
    delPW,
    findPW,
    listPW,
    genPW,
    Color,
    filename,
    filepath,
)


def test_check_file():
    check_file()
    assert os.path.exists(filepath) == True


def test_get_arg():
    os.system('python pwmngr.py -wrongArg')
    with pytest.raises(SystemExit):
        get_arg()

    os.system('python pwmngr.py -h')
    with pytest.raises(SystemExit):
        get_arg()


def test_run():
    os.system('python pwmngr.py')
    with pytest.raises(Exception):
        run()


def test_encrypt():
    assert encrypt('TextToEncrypt').endswith('==')
    assert encrypt('TextToEncrypt') != 'TextToEncrypt'
    assert len(encrypt('TextToEncrypt')) >= 50


def test_decrypt():
    assert decrypt(encrypt('TextToDecrypt')) == 'TextToDecrypt'
    assert (
        decrypt(
            'gAAAAABjZ-AbWej4r2OUwVN2iHqZ1Dxk-gDGvfW9kH8VZ78mPLqnUkyUtti3b7xXnVO6I3yfFMRIVhCPjC2MZbY6_gJi9kcvig=='
        )
        == 'TextToDecrypt'
    )


def test_newPW():
    newPW('service', 'myemail@dom.com', 'mypassword')
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'service':
                assert row[0] == 'service'


def test_editPW():
    newPW('service2', 'email@dom.com', 'mypassword')
    editPW('service2', 'newemail@dom.com', 'mynewpassword')
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'service2' and row[1] == 'newemail@dom.com':
                assert row[0] == 'service2' and row[1] == 'newemail@dom.com'


def test_delPW():
    newPW('service3', 'email@dom.com', 'mypassword123')
    delPW('service3')
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != 'service3':
                assert row[0] != 'service3'


def test_findPW():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    findPW('service')
    sys.stdout = sys.__stdout__
    assert (
        capturedOutput.getvalue()
        == f'{Color.BOLD}Name: {Color.ENDC}{Color.OKBLUE}service{Color.ENDC}\t{Color.BOLD}Email: {Color.ENDC}{Color.OKBLUE}myemail@dom.com\t{Color.ENDC}{Color.BOLD}Password: {Color.ENDC}{Color.OKBLUE}mypassword{Color.ENDC}\n'
    )


def test_listPW():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    listPW()
    sys.stdout = sys.__stdout__
    assert len(capturedOutput.getvalue()) > 200


def test_genPW():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    genPW(21, 'r', 'y')
    sys.stdout = sys.__stdout__
    assert len(capturedOutput.getvalue()) == 32
    str = (capturedOutput.getvalue())[6:-5]
    assert len(str) == 21
    assert capturedOutput.getvalue() == f'\n{Color.OKGREEN}{str}{Color.ENDC}\n'
