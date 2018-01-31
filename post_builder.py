#!/usr/bin/env python3
from string import ascii_uppercase,digits
import random


class bcolors:
    BLUEZ = '\033[34m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tst = """ \ """
kek = tst.replace(' ', '')
fkme = (kek + 'n')

def id_generator(size=6, chars=ascii_uppercase + digits):
    return ''.join(random.choice(chars) for _ in range(size))

def classic():
    INT_PARAM = int(input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC + 'How many post-params? => '))
    INT_MREQUESTS = int(input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC + 'How many requests? => '))
    URL = input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC + 'Post-Target URL => ')
    i = 1


    JUNK = str("postdata = {")

    while (i != INT_PARAM):
            THIS_PARAM = input(bcolors.HEADER + '[+] '+ bcolors.ENDC + 'Param {}: '.format(i))
            THIS_PARAM_VALUE = input(bcolors.HEADER + '[+] '+ bcolors.ENDC + 'Param {} value: '.format(i))
            JUNK += "'" + THIS_PARAM + "'" + ": '" + THIS_PARAM_VALUE + "',"
            i += 1

    THIS_PARAM = input(bcolors.HEADER + '[+] '+ bcolors.ENDC + 'Param {}: '.format(i))
    THIS_PARAM_VALUE = input(bcolors.HEADER + '[+] '+ bcolors.ENDC + 'Param {} value: '.format(i))
    JUNK += " '" + THIS_PARAM + "'" + ": '" + THIS_PARAM_VALUE + "'}"

    JUNK_POST_DATA = str("""
# This code is auto-generated by post-builder

import requests

manyrequests = int({})
i=0

{}

while (i != manyrequests):
    AJAX_POST = requests.post('{}', data=postdata)
    print(AJAX_POST)
    i+=1
    """.format(INT_MREQUESTS,JUNK,URL))
    rnd = id_generator()
    filename = rnd + ".py" 
    with open(filename, 'a') as out:
        out.write(JUNK_POST_DATA)

    print(bcolors.OKBLUE + '[+] '+ bcolors.ENDC + 'Wrote script to {}'.format(filename))

def classicchecking():
    INT_PARAM = int(2)
    TXT_LIST = input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'Text List => ')
    TXT_SPLITTER = input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'What is between user and pass? (e.g user:pass = :) => ')
    LIVE_MSG = input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'Confirmation message (e.g "Login Successful") => ')
    URL = input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'Post-Target URL => ')
    i = 1


    JUNK = str("postdata = {")

    while (i != INT_PARAM):
            THIS_PARAM = input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'User param name => ')
            JUNK += "'" + THIS_PARAM + "'" + ": " + 'suser' + ","
            i += 1

    THIS_PARAM = input(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'Pass param name =>')
    JUNK += " '" + THIS_PARAM + "'" + ": " + 'spass' + "}"

    JUNK_POST_DATA = str("""
# This code is auto-generated by post-builder

import requests

lista = open('{}', 'r').readlines()
lista = [line.replace('{}','') for line in lista]





for line in lista:
    splitlist = line.split('{}')
    suser = splitlist[0]
    spass = splitlist[1]
    {}
    AJAX_POST = requests.post('{}', data=postdata).text
    if '{}' in AJAX_POST:
        print(suser + ' ' + spass)
    else:
        print('fail' + suser + ' ' + spass)
    """.format(TXT_LIST,fkme,TXT_SPLITTER,JUNK,URL,LIVE_MSG))
    rnd = id_generator()
    filename = rnd + ".py" 
    with open(filename, 'a') as out:
        out.write(JUNK_POST_DATA)

    print(bcolors.OKBLUE + '[+] '+ bcolors.ENDC + 'Wrote script to {}'.format(filename))

def fakecli():
    fake_cli = str(input('pbuilder> '))


    if(fake_cli == '1'):
        print(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'Classic Mode.')
        classic()
    elif(fake_cli == '2'):
        print(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'Classic-Checker Mode.')
        classicchecking()
    elif(fake_cli == 'exit' or fake_cli == 'exit()' or fake_cli == 'end'):
        print(bcolors.OKGREEN + '[+] '+ bcolors.ENDC +'Exiting pbuilder...')
        exit()
    else:
        fakecli()


banner = ("""{}
           __          _ __    __         
    ____  / /_  __  __(_) /___/ /__  _____      +---------+
   / __ \/ __ \/ / / / / / __  / _ \/ ___/      | Version | 
  / /_/ / /_/ / /_/ / / / /_/ /  __/ /          +---------+
 / .___/_.___/\__,_/_/_/\__,_/\___/_/           | v0.0.2  |
/_/                                             +---------+ 
{} 
                            

            {}[i] {}https://github.com/LuanDevecchi/postbuilder

                        made with {}♥{} in Brazil                                                       

{}[!] {}Mode 1 - Classic (Simple Post Request)

{}[!] {}Mode 2 - Classic-Checker (Simple account:pass)

""".format(bcolors.BLUEZ,bcolors.ENDC,bcolors.OKBLUE,bcolors.ENDC,bcolors.WARNING,bcolors.ENDC,bcolors.OKGREEN,bcolors.ENDC,bcolors.OKGREEN,bcolors.ENDC))
print(banner)

fakecli()
