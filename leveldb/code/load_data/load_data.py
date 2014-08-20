#coding: utf-8

import random

import requests


def main():
    charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for _ in xrange(1000000):
        key = ''.join(random.sample(charSet, 20))
        value = ''.join(random.sample(charSet, 30))
        resp = requests.get('http://127.0.0.1:8799/leveldb?action=set&key=' + key + '&value=' + value)
        print resp.status_code


if __name__ == '__main__':
    main()
