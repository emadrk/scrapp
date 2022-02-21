import requests
import time


with open("folder/doubtnut.txt", "r") as file:
	links = file.readlines()
# file1 = open("brainly.txt","r")
# links = file1.readlines()
print(links)
count = 1
for link in links:
    
    url=f"{link}"
    print(url)
    # r = requests.get(url)
    #print(r.text)

    count = str(count)
    suffix = ".txt"


    x = count + suffix


    open(x, 'wt').write(url)
    # time.sleep(1)
    count= int(count)+ 1