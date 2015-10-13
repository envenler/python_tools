import datetime
import time
import os
import urllib2
import json
import urllib
import time



contactfile = open("format.txt")
lines = contactfile.readlines()
contacts = {}
for line in lines:
    person = line.split(' ')
    contacts[person[1]] = person
 
path = "./"  
url = "http://api.wwei.cn/wwei.html?data=%(data)s&version=1.0&apikey=20151012142603"  
name = "./%(name)s.png"
carddata = "MECARD:N:%(name)s;TEL:%(tel)s;ORG:%(dpt)s;NOTE:QQ:%(qq)s;"
c1 = "MECARD:N:"
c2 = ";TEL:"
c3 = ";ORG:"
c4 = ";NOTE:QQ:"
c5 = ";"
for key in contacts.keys():
    person = contacts.get(key)
    print person[1]
    
    name2 = person[1]
    dpt = person[2]
    
    data = c1+name2+c2+person[3]+c3+dpt+c4+person[4]+c5
    data = urllib2.quote(data)
    url2 = url%{"data":data}

    request = urllib2.Request(url2)
    request.add_header('User-Agent', 'ie-client')
    response = urllib2.urlopen(request)
    rspdata = response.read()
    jsondata = json.loads(rspdata)
    picdata = jsondata.get("data")
    picurl = picdata.get("qr_filepath")
    request = urllib2.Request(picurl)
    request.add_header('User-Agent', 'ie-client')
    response = urllib2.urlopen(request)
    name2 = name % {"name":person[1]}
    f = open(name2,'wb')  
    f.write(response.read())  
    f.close()
    time.sleep(1)
print "finished"

    
    

