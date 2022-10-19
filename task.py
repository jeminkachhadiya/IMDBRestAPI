
from bs4 import BeautifulSoup
import requests
import re
import sqlite3
import itertools
from datetime import datetime
import locale
import time
try:
    conn = sqlite3.connect('imdb.db')
except Error as e:
    print(e)

# Download IMDB's Top 250 data
url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
bad_chars = [';', ':', '!', "*","\n","[","]","(",")","\\n"]
movies = soup.select('td.titleColumn')

links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
#print(links)
movietitle = [a.string for a in soup.select('td.titleColumn a')]

ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
#print(ratings)



newlist=[]
#for i in range(250):
#    newdata=[movietitle[i],ratings[i]]
#    newlist.append(newdata)
#print(newlist[0][0])
#for i in range(250):
#    cur.execute(sql,newlist[i])
imdb = []
mylist=[]
rd=[]
dur=[]
desc=[]
c=0
for link in links:
    newurl = 'https://www.imdb.com'+link
    response=requests.get(newurl)
    #print("hello")
    soup1 = BeautifulSoup(response.text,'lxml')
    releasedate= [a.string for a in soup1.select('.subtext a')]
    releasedate=releasedate[-1]
#    print(releasedate)

    for i in bad_chars:
        releasedate = releasedate.replace(i, '')
    print(releasedate)
    rd.append(releasedate)
#    date_object = datetime.strptime(releasedate, '%d %B %Y %A').date()
#    print(type(date_object))
#    print(date_object)



    datetie = [a.string for a in soup1.select('.subtext time')]
#    print(datetie)


    s=(str(datetie))
    for i in bad_chars:
        s = s.replace(i, '')
    dur.append(s)
#   print(dur)
    summarytext = [c.string for c in soup1.select('.summary_text')]
#    print(summarytext)
    y = str(summarytext)
    for i in bad_chars:
        y = y.replace(i, '')

    desc.append(y)
#    print(desc)
    c+=1
    print("wait i am getting data from site")
    print(c)

#    my=[releasedate,datetie,summarytext]
#    mylist.append(my)
#    print(mylist)
for i in range(250):
    newdata=[movietitle[i],ratings[i],rd[i],dur[i],desc[i]]
    newlist.append(newdata)
print(newlist)
cur = conn.cursor()
sql = ''' INSERT INTO MOVIES(TITLE,RATING,RELEASEDATE,DURATION,DESCRIPTION)
              VALUES(?,?,?,?,?) '''
for i in range(250):
    cur.execute(sql,newlist[i])

# Store each item into dictionary (data), then put those into a list (imdb)

conn.commit();
print("completed")
