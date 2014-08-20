#coding: utf-8

import random

import requests


def main():
    charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for index in xrange(1000000):
        print index
        key = ''.join(random.sample(charSet, 20))
        value = ''.join(random.sample(charSet, 30))
        print key, value
        resp = requests.get('http://127.0.0.1:8799/leveldb?action=set&key=' + key + '&value=' + value)
        print resp.status_code
        if resp.status_code == 200:
            print resp.json()

if __name__ == '__main__':
    main()
