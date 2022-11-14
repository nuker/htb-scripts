#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import hashlib
import sys
import time

def getstr():
        headers = {"Cookie":"PHPSESSID=xxxxxxxxxxxxxxxxxxxxxx"}
        r = requests.get("http://127.0.0.1:10000")
        print(f"[<<] Getting string..\n")
        page = r.text
        soup = BeautifulSoup(page,'html.parser')
        string = soup.h3.text
        return string

def md5e(string):
        print(f"[<<] Encrypting..\n")
        md5 = hashlib.md5(string.encode())
        md5 = md5.hexdigest()
        print(f"[<<] Ready!: {md5}\n")
        return md5

def postmd5(hash):
        headers = {"Cookie":"PHPSESSID=xxxxxxxxxxxxxxxxxxxxxx"}
        data = {"hash":f"{hash}"}
        r = requests.post("http://127.0.0.1:10000", data=data)
        print(r.text)

def run():
        string = getstr()
        md5 = md5e(string)
        postmd5(md5)

if __name__ == "__main__":
        run()
