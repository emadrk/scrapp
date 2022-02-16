# import library
# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
# import beautifulsoup4
# Request to website and download HTML contents
url='https://zollege.in/exams/jee-main'
req=requests.get(url)
content=req.content

soup=BeautifulSoup(content)

tag = soup.body
file = open("output1.txt", "a")
for string in tag.strings:
    file.write(string)
    file.write("\n")
file.close()    



