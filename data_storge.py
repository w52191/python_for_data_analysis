
# coding: utf-8

# In[4]:

get_ipython().system(u'cat ch06/ex1.csv')


# In[1]:

from lxml.html import parse
from urllib2 import urlopen


# In[2]:

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))


# In[3]:

doc = parsed.getroot()


# In[4]:

links = doc.findall('.//a')


# In[5]:

links[15:20]


# In[6]:

lnk = links[28]


# In[7]:

lnk


# In[8]:

lnk.get('href')


# In[9]:

lnk.text_content()


# In[10]:

urls = [lnk.get('href') for lnk in doc.findall('.//a')]


# In[11]:

urls[-10:]


# In[12]:

tables = doc.findall('.//table')


# In[13]:

calls = tables[2]


# In[14]:

puts = tables[1]


# In[15]:

rows = calls.findall('.//tr')


# In[16]:

def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]


# In[17]:

_unpack(rows[0], kind='th')


# In[18]:

_unpack(rows[1], kind='td')


# In[21]:

from pandas.io.parsers import TextParser


# In[23]:

def parse_options_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()


# In[24]:

call_data = parse_options_data(calls)


# In[25]:

put_data = parse_options_data(puts)


# In[26]:

call_data[:10]


# In[31]:

#Interacting with HTML and Web APIs
import requests
url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)


# In[32]:

resp


# In[33]:

import json
data = json.loads(resp.text)
data.keys()


# In[35]:

#Interacting with databases
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER
);"""


# In[36]:

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()


# In[37]:

data = [('Atlanta', 'Georgia', 1.25, 6),
('Tallahassee', 'Florida', 2.6, 3),
('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()


# In[38]:

cursor = con.execute('select * from test')


# In[39]:

rows = cursor.fetchall()


# In[40]:

rows


# In[41]:

cursor.description


# In[43]:

from pandas import DataFrame
DataFrame(rows, columns=zip(*cursor.description)[0])


# In[44]:

import pandas.io.sql as sql


# In[45]:

sql.read_frame('select * from test', con)


# In[ ]:



