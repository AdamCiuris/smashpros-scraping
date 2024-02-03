# https://smashpros.gg/api/sets/user/x/complete?limit=9999999999

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


cookies = {
    'connect.sid': 's%3AbmZQC_NHchqSOgDjLreoR60gQ-pZGqNs.WLFfG6d9Bktjuc1TGYurnvp1fhhP8W2wemYkb%2BVtPNc',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'connect.sid=s%3AbmZQC_NHchqSOgDjLreoR60gQ-pZGqNs.WLFfG6d9Bktjuc1TGYurnvp1fhhP8W2wemYkb%2BVtPNc',
    'Origin': 'https://smashpros.gg',
    'Referer': 'https://smashpros.gg/matchmaking',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

json_data = {
    'text': 'like smogon',
}

# curl 'https://smashpros.gg/api/sets/1b52535e-90f3-4e2d-913f-2c8f5350a12d/messages' \
#   -H 'Accept: application/json, text/plain, */*' \
#   -H 'Accept-Language: en-US,en;q=0.7' \
#   -H 'Connection: keep-alive' \
#   -H 'Content-Type: application/json' \
#   -H 'Cookie: connect.sid=s%3AbmZQC_NHchqSOgDjLreoR60gQ-pZGqNs.WLFfG6d9Bktjuc1TGYurnvp1fhhP8W2wemYkb%2BVtPNc' \
#   -H 'Origin: https://smashpros.gg' \
#   -H 'Referer: https://smashpros.gg/matchmaking' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Sec-GPC: 1' \
#   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Linux"' \
#   --data-raw '{"text":"like smogon"}' \
#   --compressed

cpus = os.cpu_count()
mostRecentTimeout = 0
def scrape(ids,outputFolder,threadNum):
    s = requests.Session()
    retries = Retry(total=None, backoff_factor=.1, status_forcelist=[500,502,503,504])
    s.mount('https://', HTTPAdapter(max_retries=retries))
    with open(pwd/ str(threadNum), 'w+') as debugfile:
        debugID = 1
        for i in ids:
            print('scraping messages from set id: ', i)
            try:
                response = s.get(f'https://smashpros.gg/api/sets/current/{i}' , cookies=cookies, headers=headers, timeout=None,)
                ezpz = json.loads(response.content)
                a= json.dumps(ezpz, indent=4)
                time = datetime.now()
                with open(f'{outputFolder}/{i}.{time}.json','w+') as of:
                    of.write(str(a))
                    of.close()
            except TimeoutError as te:
                print('TimeoutError at' + str(i)+ ', previous timeout at ')
                mostRecentTimeout = i
                ids.append(i)
            except ConnectTimeoutError as cte:
                print('ConnectTimeoutError at' + str(i)+ ', previous timeout ' )
                mostRecentTimeout = i
                ids.append(i)
                
            except Exception as e:
                print('general exception: '+e+' at ' + str(i))
                ids.append(i)
            debugfile.write(f'{i}_{debugID},\n')
            debugID+=1
        print('finished ids: ', ids)
    debugfile.close()





def matchIDs(symDiffIds):
    with open(symDiffIds, 'r+') as of:
          cont = of.readlines()
    lol = []
    for line in cont:
         lol.append(line.split(',')[0])
    return lol
    
def run(symDiffIds,outputFolder):
    ts  = []
    allIds = matchIDs(symDiffIds)
    idStart, idEnd = 0, len(allIds)
    
    divs = (idEnd-idStart)//cpus # TODO causes issues when fewer ids than cpus
    remainder = (idEnd-idStart)%cpus
    startEnds = []
    st, end = 0, divs
    for i in range(cpus-1):
        startEnds.append((allIds[st:end]))
        st = end
        end += divs
    startEnds.append((st,end+remainder))

    tcount = 0
    for i in range(cpus):
            t = Thread(target=scrape, args=[startEnds[i],outputFolder,tcount])
            print('starting thread: ' + str(tcount) + ' with ' + str(len(startEnds[tcount])) + ' ids.')
            ts.append(t)
            t.start()
            tcount+=1

    for t in ts:
         t.join()

if __name__ == "__main__":
    symDiffIds,outputFolder = pwd/sys.argv[1], pwd/sys.argv[2]
    run(symDiffIds,outputFolder)