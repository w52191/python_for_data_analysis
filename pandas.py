
# coding: utf-8

# In[1]:

from pandas import Series, DataFrame
import pandas as pd


# In[2]:

obj = Series([4,7,-5,3])


# In[3]:

obj.values


# In[4]:

obj.index


# In[5]:

obj2 = Series([4,7,-5,3], index = ['d','b','a','c'])


# In[6]:

obj2


# In[7]:

obj2['d']


# In[9]:

obj2[['a','b','d']]


# In[10]:

obj2[obj2 > 0]


# In[12]:

obj2 * 2


# In[14]:

import numpy as np
np.exp(obj2)


# In[15]:

'b' in obj2


# In[16]:

'e' in obj2


# In[17]:

sdata = {'Ohio':35000, 'Texes':71000, 'Oregon':16000, 'Utah':5000}


# In[18]:

obj3 = Series(sdata)


# In[19]:

obj3


# In[20]:

states = ['Ohio', 'California', 'Oregon', 'Texes']


# In[21]:

obj4 = Series(sdata, index = states)


# In[22]:

obj4


# In[23]:

pd.isnull(obj4)


# In[24]:

pd.notnull(obj4)


# In[25]:

obj4.isnull()


# In[26]:

obj3 + obj4


# In[27]:

obj4.name = 'population'


# In[28]:

obj4


# In[29]:

obj4.index.name = 'state'


# In[30]:

obj4


# In[31]:

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']


# In[32]:

obj


# In[33]:

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}


# In[34]:

frame = DataFrame(data)


# In[35]:

frame


# In[36]:

DataFrame(frame, columns=['year','state','pop'])


# In[39]:

frame2 = DataFrame(data, columns = ['year','state','pop','debt'], index = ['one','two','three','four','five'])


# In[40]:

frame2.columns


# In[41]:

frame2


# In[42]:

frame2['state']


# In[43]:

frame2.state


# In[44]:

frame2.year


# In[45]:

frame2.ix['three']


# In[47]:

frame2['debt'] = 16.5


# In[48]:

frame2


# In[49]:

val = Series([-1.2,-1.5,-1.7], index = ['two','four','five'])


# In[50]:

frame2['debt'] = val


# In[51]:

frame2


# In[52]:

frame2['one','debt'] = 8


# In[53]:

frame2


# In[55]:

frame2['one'] = 8


# In[56]:

frame2


# In[67]:

frame2.ix['one', 'debt'] = 8


# In[68]:

frame2


# In[73]:

frame2.ix['seven'] = 8
frame2


# In[74]:

frame2.drop('seven')


# In[77]:

frame2 = frame2.drop('seven', axis = 1)


# In[78]:

frame2


# In[79]:

frame2['eastern'] = frame2.state == 'Ohio'


# In[80]:

frame2


# In[81]:

frame2.state


# In[82]:

obj4


# In[83]:

del frame2['eastern']


# In[84]:

frame2


# In[86]:

frame2.columns


# In[87]:

pop = {'Nevada': {2001:2.4, 2002:2.9},
       'Ohio': {2000:1.5, 2001:1.7, 2002:36}}


# In[88]:

frame3 = DataFrame(pop)


# In[89]:

frame3


# In[90]:

frame3.T


# In[91]:

frame3.name = 'test'


# In[92]:

frame3


# In[93]:

frame3.name


# In[94]:

DataFrame(pop, index = [2001, 2002, 2003])


# In[95]:

pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}


# In[96]:

pdata


# In[97]:

DataFrame(pdata)


# In[98]:

frame3.index.name = 'year'


# In[99]:

frame3


# In[100]:

frame3.columns.name = 'state'


# In[101]:

frame3


# In[102]:

frame3.values


# In[103]:

frame2.values


# In[104]:

frame2


# In[105]:

obj = Series(range(3), index = ['a', 'b', 'c'])


# In[106]:

index = obj.index


# In[107]:

index


# In[108]:

index[1:]


# In[111]:

index = pd.Index(np.arange(3))


# In[112]:

index


# In[113]:

obj2 = Series([1.5,-2.5,0], index = index)


# In[114]:

obj2


# In[115]:

frame3


# In[116]:

'Ohio' in frame3.columns


# In[117]:

2003 in frame3.index


# In[ ]:



