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





# output = soup.get_text()

# for row in output.splitlines():
#     if row.find_all('p'):
#         data = row.find_all('p')
#         a = data.get_text()
#         file = open("output1.txt", "a")
#         file.write(a)
#         file.write("\n\n")
#         file.close() 

# table1 = soup.find("table", border=1)
# table2 = soup.find('tbody')
# tables = soup.find_all('tr')

# for td in tables:
#     # rn = soup.find_all("td")[0].get_text()
#     rn = soup.find_all("td")
#     for element in rn:
#         file = open("output.txt", "a")
    
#         file.write(element.get_text())
#         file.write("\n")
#         file.close() 


    # sr = soup.find_all("td")[1].get_text()
    # d = soup.find_all("td")[2].get_text()
    # n = soup.find_all("td")[3].get_text()

    # print(rn + "," + sr + "," + d + ",", file=f)



















































# # soup = soup.prettify()
# # print(soup)
# # emad = soup.prettify()
# # emad = soup.get_text()
# # heading = soup.find_all('h2')
# # print(heading)
# # emad = soup.get_text()
# # file = open("out.txt", "w")
# # file.write(emad)
# # file.close()


# # data = '' 
# # for data in soup.find_all("p"): 
# #     print(data.get_text()) 


# # for e in soup :
# #     a = ['tr',]
# #     rows = e.find_all('tr')
# #     for tr in rows:
# #         for z in tr.children:
# #             if z.name == 'td':
# #                 do somthing
# #             elif z.name == 'th':
# #                 do something
# #             elif z.name == 'p':
# #                 do something




# #   if e["class"] == "pickmenucolmenucat" :
# #     output.append(e)
# #   if e["class"] == "pickmenucoldispname" :
# #     output.append(e)
# #   if e["class"] == "pickmenucolportions" :
# #     output.append(e)    


# divs = soup.find_all('div')

# for each in divs:
#     if each.find('tr'):
#         a = each.find('tr')
#         file = open("output.txt", "a")
#         for elements in str(a.contents):
#             file.write(elements)
#         file.write("\n")
#         file.close() 
#     if each.find('td'):
#         a = each.find('td')
#         file = open("output.txt", "a")
#         for elements in str(a.contents):
#             file.write(elements)
#         file.write("\n")
#         file.close()   
#     if each.find('th'):
#         a = each.find('th')
#         file = open("output.txt", "a")
#         for elements in str(a.contents):
#             file.write(elements)
#         file.write("\n")
#         file.close()   
#     if each.find('head'):
#         a = each.find('head')
#         file = open("output.txt", "a")
#         file.write(a.contents)
#         file.write("\n")
#         file.close()
#     if each.find('title'):
#         a = each.find('title')
#         file = open("output.txt", "a")
#         file.write(a.contents)
#         file.write("\n")
#         file.close()    
#     if each.body:
#         if each.body.find('b'):
#             a = each.body.find('b')
#             file = open("output.txt", "a")
#             file.write(a.contents)
#             file.write("\n")
#             file.close() 
#     if each.find('a'):
#         # alpha= each.a.find_all('a')
#         a = each.find('a')
#         file = open("output.txt", "a")
#         file.write(str(each.a.contents[0]))
#         file.write("\n")
#         file.close() 
#     # if each.head:
#     #     alpha=each.head
#     #     for child in alpha:
#     #         file = open("output.txt", "a")
#     #         file.write(alpha)
#     #         file.write("\n")
#     #         file.close() 


        






