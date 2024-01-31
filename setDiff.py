import requests
import json
import os, sys
from pathlib import Path
from datetime import datetime
from threading import Thread
from multiprocessing import Pool, TimeoutError
from threading import Thread
from urllib3.exceptions import ConnectTimeoutError
from requests.adapters import HTTPAdapter, Retry
pwd = Path(__file__).parent 


def compare(one, two):
    return set(one).symmetric_difference(set(two))


def matchIDs():
    with open( pwd/'matchIds'/'allasof012924uniques', 'r+') as of:
          cont = of.readlines()
    lol = []
    for line in cont:
         lol.append(line.split(',')[0])
    return lol

def writeDiffs(y):
    y = list(y)
    with open(pwd/'missedIDs'/'missedIds', 'w+') as of:
          for id in y:
            cont = of.write(f'{id},\n')


if __name__ == "__main__":
    ALREADYREADIDS = os.listdir(pwd / '3rd')
    oldIds = list(map(lambda x: x.split('.')[0], ALREADYREADIDS))

    ALLIDS = matchIDs()
    y =compare(ALLIDS, oldIds)
    writeDiffs(y)
