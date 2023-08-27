# import requests
# import json





# for i in range(1,200):
#     with open('config.json','r') as file:
#         config = file.read()
#         config = json.loads(config)
#     api_key = config['api_key']
#     response = requests.get(
#         "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page="+str(i)+"&page_size=10",
#         headers ={ "Authorization": f"Token {api_key}"}
#     )
#     #print(response.json())
#     result = response.json()['results']
#     #print(type(result))




#     json_data = json.dumps(result)

#     proxies = []
#     for proxy in result:
#         print(proxy)
#         prox = proxy['username']+':'+proxy['password']+'@'+proxy['proxy_address']+':'+str(proxy['port'])
#         proxies.append(prox)


#     with open('proxies.txt', 'a') as file:
#         for proxy in proxies:
#             file.write(proxy+'\n')

import requests
import json






with open('config.json','r') as file:
        config = file.read()
        config = json.loads(config)
api_key = config['api_key']
response = requests.get(
        "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=1000",
        headers ={ "Authorization": f"Token {api_key}"}
    )
    #print(response.json())
result = response.json()['results']
    #print(type(result))




json_data = json.dumps(result)

proxies = []
for proxy in result:
        print(proxy)
        prox = proxy['username']+':'+proxy['password']+'@'+proxy['proxy_address']+':'+str(proxy['port'])
        proxies.append(prox)


with open('proxies.txt', 'a') as file:
        for proxy in proxies:
            file.write(proxy+'\n')