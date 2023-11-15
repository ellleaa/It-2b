import requests

#urlopen(https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat)
#webbrowser.open ('https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat') 
for i in range(1,1000000000):

# 

    # response = requests.geft('https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat?d={i}')
    response = requests.get(f'https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat?d={i}')
    # print (response.status_code)
    # print (response.content)
    # print (response.text)

    for line in response.text.splitlines():
        line = line.strip()
        if line.startswith("<title>"):
            print(line)
            break


# https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat?d=1
