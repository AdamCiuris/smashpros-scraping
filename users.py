import json
import requests
import uncurl
# curl 'https://smashpros.gg/api/users/shinymark1' 
    # 'Accept':'application/json, text/plain, */*' 
    # 'Accept-Language':'en-US,en;q=0.9' 
    # 'Connection':'keep-alive' 
    # 'Cookie':'_ga=GA1.1.2039137305.1706400722; connect.sid=s%3AR_blPN_-rRMb3unS-wN4WHY0jbrFl6m7.DRCfdzJUXilZZpumeekXFhhQR%2FsTlaa1kvhR2NBi5y8; _ga_W6ZL09PE1Y=GS1.1.1706484888.3.1.1706484898.0.0.0' 
    # 'Referer':'https://smashpros.gg/user/shinymark1' 
    # 'Sec-Fetch-Dest':'empty' 
    # 'Sec-Fetch-Mode':'cors' 
    # 'Sec-Fetch-Site':'same-origin' 
    # 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' 
    # 'sec-ch-ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' 
    # 'sec-ch-ua-mobile':'\?0' 
    # 'sec-ch-ua-platform':'\"Linux\"' 
#       
  
# curl 'https://smashpros.gg/api/users/shinymark1' \
#   -H 'Accept: application/json, text/plain, */*' \
#   -H 'Accept-Language: en-US,en;q=0.9' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: _ga=GA1.1.2039137305.1706400722; connect.sid=s%3AR_blPN_-rRMb3unS-wN4WHY0jbrFl6m7.DRCfdzJUXilZZpumeekXFhhQR%2FsTlaa1kvhR2NBi5y8; _ga_W6ZL09PE1Y=GS1.1.1706484888.3.1.1706484898.0.0.0' \
#   -H 'Referer: https://smashpros.gg/user/shinymark1' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Linux"' \
#   --compressed


curH = """curl 'https://smashpros.gg/api/users/shinymark1' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: _ga=GA1.1.2039137305.1706400722; connect.sid=s%3AR_blPN_-rRMb3unS-wN4WHY0jbrFl6m7.DRCfdzJUXilZZpumeekXFhhQR%2FsTlaa1kvhR2NBi5y8; _ga_W6ZL09PE1Y=GS1.1.1706484888.3.1.1706484898.0.0.0' \
  -H 'Referer: https://smashpros.gg/user/shinymark1' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
"""




h = eval(uncurl.parse(curH))
ezpz = json.loads(h.content)
a= json.dumps(ezpz, indent=4)
# r = requests.get('hatps://smashpros.gg/user/shinymark1')

with open('./first.json','w+') as of:
    of.write(str(a))

# print(r)