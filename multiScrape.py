# https://smashpros.gg/api/sets/user/x/complete?limit=9999999999
# headers and cookie made with curl converter website
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
jsonDump = Path(__file__).parent /'multiSets'

cookies = {
    'connect.sid': 's%3AbmZQC_NHchqSOgDjLreoR60gQ-pZGqNs.WLFfG6d9Bktjuc1TGYurnvp1fhhP8W2wemYkb%2BVtPNc',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'connect.sid=s%3AbmZQC_NHchqSOgDjLreoR60gQ-pZGqNs.WLFfG6d9Bktjuc1TGYurnvp1fhhP8W2wemYkb%2BVtPNc',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'limit': '20',
}
cpus = os.cpu_count()

def scrape(idStart, idEnd):
    mostRecentTimeout = 0
    s = requests.Session()
    retries = Retry(total=None, backoff_factor=.2, status_forcelist=[500,502,503,504]) 
    # forces retry on err code 500 502 503 504
    # .1 backoff does .05 .1 .2 .4 seconds between retries
    s.mount('https://', HTTPAdapter(max_retries=retries))
    for i in range(idStart,idEnd):
        try:
            response = s.get(f'https://smashpros.gg/api/sets/user/{i}/complete', params=params, cookies=cookies, headers=headers, timeout=None,)
            ezpz = json.loads(response.content)
            a= json.dumps(ezpz, indent=4)
            time = datetime.now()
            with open(f'{jsonDump}/{i}.{time}.json','w+') as of:
                of.write(str(a))
                of.close()
        except TimeoutError as te:
            print('TimeoutError at' + str(i)+ ', previous timeout at ' + str(mostRecentTimeout))
            mostRecentTimeout = i
            i = i -1
        except ConnectTimeoutError as cte:
            print('ConnectTimeoutError at' + str(i)+ ', previous timeout at ' + str(mostRecentTimeout))
            mostRecentTimeout = i
            i = i -1

if __name__ == "__main__":
    ts  = []
    idStart, idEnd = 0, 30000
    
    divs = (idEnd-idStart)//cpus
    remainder = (idEnd-idStart)%cpus
    startEnds = []
    st, end = 0, divs
    for i in range(cpus-1):
        startEnds.append((st,end))
        st = end
        end += divs
    startEnds.append((st,end+remainder))


    for i in range(cpus):
            t = Thread(target=scrape, args=[startEnds[i][0],startEnds[i][1]])
            t.start()
            ts.append(t)

    for t in ts:
         t.join()