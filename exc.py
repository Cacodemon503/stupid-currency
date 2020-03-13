#!/usr/bin/python3
from playsound import playsound
import threading
import requests
import time
import sys
import os


def currency():
    r_usd = requests.get('https://api.ratesapi.io/api/latest?base=USD&symbols=RUB')
    r_eur = requests.get('https://api.ratesapi.io/api/latest?base=EUR&symbols=RUB')
    usd_cost = r_usd.json()['rates']['RUB']
    eur_cost = r_eur.json()['rates']['RUB']
    return(usd_cost, eur_cost)


def no_connect():
    try:
        yellow = '\033[93m'
        endcolor = '\033[0m'
        print(f'{yellow}Please, check your internet connection{endcolor} ...')
        time.sleep(2)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.exit()
    except KeyboardInterrupt:
        kill()


def kill():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print('Program killed by user')
    time.sleep(0.5)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.exit()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def sound():
    playsound(resource_path('drum.wav'))


if __name__ == '__main__':
    try:
        t1 = threading.Thread(target=sound)
        t1.start()
        usd_cost, eur_cost = currency()
        yel = '\033[93m'
        end = '\033[0m'
        print(f'{yel}USD{end}: {usd_cost} RUB')
        print(f'{yel}EUR{end}: {eur_cost} RUB')
        time.sleep(2)
        t1.join()
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
    except(requests.exceptions.ConnectionError):
        no_connect()
    except KeyboardInterrupt:
        kill()
