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


def matchIDs(newIds):
    """needs all unique match ids that have already been run,"""
    with open( newIds, 'r+') as of:
          cont = of.readlines()
    lol = []
    for line in cont:
         lol.append(line.split(',')[0])
    return lol

def writeDiffs(symdiff, symDiffIdsOutputFolderFile):
    symdiff = list(symdiff)
    with open(symDiffIdsOutputFolderFile, 'w+') as of:
          for id in symdiff:
            cont = of.write(f'{id},\n')

def run(oldIds, newIds,symDiffIds):
    ALREADYREADIDS = os.listdir(oldIds)
    oldIds = list(map(lambda x: x.split('.')[0], ALREADYREADIDS))

    ALLIDS = matchIDs(newIds)
    symdiff =compare(ALLIDS, oldIds)
    writeDiffs(symdiff, symDiffIds)

if __name__ == "__main__":
    oldIds, newIds, symDiffIds = pwd/sys.argv[1],pwd/sys.argv[2],pwd/sys.argv[3]
    res = run(oldIds, newIds,symDiffIds)

