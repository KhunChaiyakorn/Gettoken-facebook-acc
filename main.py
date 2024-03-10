#!/bin/python3
# -*- coding: utf-8 -*-

import json
import requests
from getpass import getpass as pw
from os import system as st
from os import mkdir as dir
from time import sleep as sp

def main():
    b3 = input(' wana watch u token? : [y] , [n] ')
    if b3 == 'y':
        _ashs_()
        user_id()
        print('\n\n [-]====[ Facebook ]====[-]')
    elif b3 == 'n':
        exit()

def _ashs_():
    try:
        id = input(' Email Facebook : ')
        passwd = pw(' Password : ')
        ab = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+id+"&locale=en_US&password="+passwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        cont = json.loads(ab.text)
        print('[!]==========[' + ' You Token ' + ']==========[!]')
        print(cont['access_token \n'])
    except KeyboardInterrupt:
        print('[x] Error \n\n')
    except KeyError:
        print('[x] ERROR \n\n')

def user_id():
    try:
        tok = input('\n\n Enter your Token to view ID. : ')
        url = "https://graph.facebook.com/me?access_token=%s\n" % tok
        r = requests.get(url)
        dat = json.loads(r.text)
        print('\nID Facebook : ' + dat['id'])
        print('------------')
    except KeyError:
        print('[x] Token Salah!\n\n')
    except KeyboardInterrupt:
        print('[x] Disable\n\n')
    finally:
        exit()

if __name__ == '__main__':
    try:
        main()
    except:
        exit()
