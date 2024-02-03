import requests
import json
import os, sys
import subprocess
from pathlib import Path
from datetime import datetime
from threading import Thread
from multiprocessing import Pool, TimeoutError
from threading import Thread
from urllib3.exceptions import ConnectTimeoutError
from requests.adapters import HTTPAdapter, Retry
pwd = Path(__file__).parent 

def run(userSetFolder:Path,outputFile):

    ok = r"""grep -r '"id": "' ./"""+str(userSetFolder.relative_to(pwd)) +r"""/"""
    print(ok)
    # grep = f"grep -r '\"id\": \"' ./{userSetFolder}/*\""
    daGrep = subprocess.Popen( ok,stdout=subprocess.PIPE ,shell=True).stdout.readlines()
    with open(outputFile, 'w+') as outfile:
        for line in daGrep:
            line = line.decode('utf-8')
            line = line.split('"id": ')[1].split('"')[1] #grabs id out of './completeSets/10000.2024-01-30 02:49:51.424510.json:            "id": "848b6f6f-ee19-4833-89a4-1a40b51c2219",\n'
            outfile.write(f'{line},\n')
        
    outfile.close()

if __name__ == '__main__':
    run(sys.argv[1],pwd/sys.argv[2])