
# coding: utf-8

# In[1]:

import json
import numpy as np
import pandas as pd
db = json.load(open('ch07/foods-2011-10-03.json'))


# In[2]:

len(db)


# In[3]:

db[0].keys()


# In[4]:

db[1].keys()


# In[5]:

db[0]['nutrients'][0]


# In[6]:

db[0]['nutrients'][1]


# In[7]:

len(db[0]['nutrients'])


# In[8]:

len(db[0]['nutrients'][0])


# In[10]:

from pandas import DataFrame
nutrients = DataFrame(db[0]['nutrients'])


# In[11]:

nutrients[:7]


# In[12]:

info_keys = ['description', 'group', 'id', 'manufacturer']


# In[13]:

info = DataFrame(db, columns=info_keys)


# In[14]:

info[:7]


# In[23]:

len(info.columns)


# In[25]:

info.description[0]


# In[26]:

info


# In[27]:

pd.value_counts(info.group)[:10]


# In[28]:

nutrients = []
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
#nutrients = pd.concat(nutrients, ignore_index=True)


# In[29]:

nutrients


# In[30]:

nutrients = pd.concat(nutrients, ignore_index=True)


# In[31]:

nutrients[:7]


# In[37]:

col_mapping = {'description' : 'nutrient',
'group' : 'nutgroup'}


# In[38]:

nutrients = nutrients.rename(columns=col_mapping, copy=False)


# In[39]:

nutrients[:7]


# In[46]:

ndata = pd.merge(nutrients, info, on='id', how='outer')


# In[41]:

ndata


# In[42]:

ndata.ix[30000]


# In[44]:

col_mapping = {'description' : 'food',
'group' : 'fgroup'}


# In[45]:

info = info.rename(columns=col_mapping, copy=False)


# In[47]:

result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)


# In[48]:

result[:7]


# In[49]:

ndata[:7]


# In[51]:

result['Zinc, Zn'].sort_values().plot(kind='barh')


# In[52]:

import matplotlib.pyplot as plt


# In[53]:

plt.show()


# In[ ]:



