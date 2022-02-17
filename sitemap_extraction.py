import requests
from bs4 import BeautifulSoup

wunder = requests.get("https://www.doubtnut.com/static/sos-dn-381.xml")
parcala = BeautifulSoup(wunder.content,"lxml")

links = parcala.find_all("loc")
file = open("doubtnut.txt", "a")
for x in parcala.find_all("loc"):
    file.write(x.text)
    file.write("\n")
file.close()    

