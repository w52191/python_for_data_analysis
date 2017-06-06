
# coding: utf-8

# In[2]:

#cite: Python for Data Analysis Chapter 4
import numpy as np
data1 = [6,7.8,7,8,9]
arr1 = np.array(data1)


# In[3]:

arr1


# In[13]:

np.shape(arr1)


# In[4]:

data2 = [[6,7.8,7],[8,9,10]]
arr2 = np.array(data2)


# In[5]:

arr2


# In[21]:

#np.shape(arr2)
arr2.shape


# In[20]:

arr2.dtype


# In[6]:

np.zeros(10)


# In[7]:

np.zeros((3,6))


# In[8]:

np.ones(3)


# In[9]:

ones_test = np.ones(3)


# In[12]:

np.shape(ones_test)


# In[15]:

np.empty((2,3,2))


# In[23]:

np.arange(15)


# In[24]:

np.eye(4)


# In[25]:

arr1 = np.array([1,2,3], dtype = np.float64)


# In[26]:

arr1.dtype


# In[27]:

arr2 = np.array([1,2,3], dtype  = np.int32)


# In[28]:

arr2.dtype


# In[31]:

float_arr = arr2.astype(np.float64)


# In[32]:

float_arr.dtype


# In[34]:

numeric_strings = np.array(['1.25','0.8','42'], dtype = np.string_)


# In[35]:

numeric_strings.astype(float)


# In[36]:

arr1.astype(arr2.dtype)


# In[37]:

arr1.dtype


# In[38]:

arr1


# In[39]:

arr1.astype('u4')


# In[40]:

arr = np.arange(10)


# In[43]:

arr[5]


# In[44]:

arr[5:8]


# In[45]:

arr_slice = arr[5:8]


# In[46]:

arr_slice[1] = 12345


# In[47]:

arr


# In[48]:

arr_slice[:] = 64


# In[49]:

arr


# In[52]:

arr1 = arr[5:8].copy()


# In[53]:

arr1


# In[54]:

test1 = [1, 5, 6, 4, 8]


# In[55]:

test2 = test1[1:3]


# In[57]:

test2[1] = 10


# In[58]:

test2


# In[59]:

test1


# In[60]:

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[61]:

arr2d


# In[62]:

arr2d[2]


# In[63]:

arr2d[2,0]


# In[64]:

arr2d[2][0]


# In[65]:

arr2d[:2][1:]


# In[66]:

arr2d[:2,1:]


# In[ ]:



