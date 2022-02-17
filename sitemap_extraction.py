# from bs4 import BeautifulSoup
# import requests
# import gzip
# # from StringIO import StringIO
# from io import StringIO


# def crawler():
#     url="https://brainly.in/sitemap-new.xml"
#     old_xml=requests.get(url)
#     # new_xml=gzip.GzipFile(fileobj=StringIO(old_xml.content)).read()
#     #new_xml=old_xml.text
#     # final_xml=BeautifulSoup(new_xml)
#     final_xml=BeautifulSoup(old_xml)
#     item_to_be_found=final_xml.findAll('loc')
#     file = open("output2.txt", "a")
#     for loc in item_to_be_found:
#         # count=count+1
#         file.write(loc.text)
#         file.write("\n")
#         # print(count)
#     file.close()

# crawler()

# # for loc in item_to_be_found:
# #     print item_to_be_found.index(loc) + 1, loc.text






# I need the extract links in sitemap https://wunder.com.tr/sitemap.xml

# I wrote some code

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

