
# coding: utf-8

# In[1]:

# cite: Chapter 3 in Python for Data Analysis
from numpy.random import randn


# In[3]:

data = {i: randn() for i in range(7)}


# In[4]:

data


# In[5]:

print data


# In[ ]:




# In[6]:

an_apple = 27 # test <tab>, like an<Tab>


# In[7]:

an_example = 42


# In[8]:

b = [1, 2, 3] # test <TAB>, like b.<tab>


# In[ ]:




# In[9]:

b? # test '?'


# In[10]:

def add_numbers(a, b):
    '''
    Test '??'
    '''
    return a + b


# In[16]:

get_ipython().magic(u'pinfo add_numbers')


# In[17]:

add_numbers?? #display source code


# In[18]:

import numpy as np
np.*load*? #search 'load'


# In[21]:

a = np.random.randn(100, 100)


# In[22]:

get_ipython().magic(u'timeit np.dot(a, a)')


# In[23]:

get_ipython().magic(u'pinfo %reset')


# In[ ]:



