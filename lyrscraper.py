import requests as req
import re

file = open("searcharg.txt", "r")

content = file.read()
try:
    url = "https://www.google.com/search?q=" + content
    res = req.get(url)
    data = res.text
    x = (re.search("genius.com/.*\-lyrics", data))
    genurl = x[0]
    head, sep, tail = genurl.partition('&')
    url2 = 'https://' + head
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

print(url2)
