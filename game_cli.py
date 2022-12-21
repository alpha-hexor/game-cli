import httpx
import re
import os
from torrent import Torrent as t

#global shit
MAIN_URL = "https://crotorrents.com"
MAX_PAGE = 11
client = httpx.Client(headers={'user-agent':'uwu'})
GAME_REGEX = r'href="https://crotorrents.com/(.*?)-torrent-(.*?)download/"'
REQUIREMENT = r"<strong>(.*)</strong>(.*)</li>"
MAGNET = r"magnet:\?xt=urn:btih:[a-zA-Z0-9]*"
TORRENT_CREDS = "admin:adminadmin"
savepath = f"{os.getcwd()}\\downlaods"

try:
    os.mkdir(savepath)
except:
    pass


m=t()

game_links = []


name = input("[*]Enter game: ").replace(" ","+")
for i in range(MAX_PAGE):
    r=client.get(f"{MAIN_URL}/page/{i}/?s={name}")
    if r.status_code == 404:
        break
    game_links +=re.findall(GAME_REGEX,r.text)
    
game_links = list(set(game_links)) #get rid of the duplicates
if len(game_links) == 0:
    print("[*]No games found")
    exit()
#display result
for index , game in enumerate(game_links,start=1):
    print(f"{index} : {game[0]}")
    
x = int(input("[*]Enter index: "))
game_name , keyword = game_links[x-1]

#get requirements and magnet links
r=client.get(f"{MAIN_URL}/{game_name}-torrent-{keyword}download/")
requirements = re.findall(REQUIREMENT,r.text)

print("\n\n========System Requirements=========")
for req in requirements:
    print(f"{req[0]} {req[1]}")
    
magnet=re.findall(MAGNET,r.text)[0]

if(m.login(username=TORRENT_CREDS.split(":")[0],password=TORRENT_CREDS.split(":")[-1])):
    if(m.add_link(magnet_link=magnet,save_path=savepath)):
        print("[*]Game is added to the torrrent successfully")
    else:
        print("[-]Can't add to the torrent")
else:
    print("[-]Please check torrent creds and try again")
    exit()
    
    