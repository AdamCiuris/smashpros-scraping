# https://smashpros.gg/api/sets/user/x/complete?limit=9999999999
import requests
import json
from pathlib import Path
from datetime import datetime
from urllib3.exceptions import ConnectTimeoutError
from requests.adapters import HTTPAdapter, Retry



jsonDump = Path(__file__).parent /'completeSets'

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
proxy = {
    'http':  'socks5://localhost:9050',
    'https': 'socks5://localhost:9050',
}

params = {
    'limit': '99999999',
}

mostRecentTimeout = 0
s = requests.Session()
retries = Retry(total=None, backoff_factor=.1, status_forcelist=[500,502,503,504])
s.mount('https://', HTTPAdapter(max_retries=retries))
for i in range(9463,30000):
    try:
        response = s.get(f'https://smashpros.gg/api/sets/user/{i}/complete', params=params, proxies=proxy, cookies=cookies, headers=headers, timeout=None,)
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