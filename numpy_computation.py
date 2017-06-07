
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


# In[3]:

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])


# In[9]:

from numpy.random import randn
data = randn(7,4)


# In[10]:

names == 'Bob'


# In[11]:

data


# In[12]:

data[names == 'Bob']


# In[13]:

data[names == 'Bob', 2:]


# In[14]:

data[names == 'Bob', 3]


# In[15]:

names != 'Bob'


# In[17]:

data[~(names == 'Bob')]


# In[18]:

mask = (names == 'Bob')|(names == 'Will')


# In[19]:

data[mask]


# In[20]:

data[data < 0] = 0


# In[21]:

data


# In[23]:

data[names != 'Joe'] = 7


# In[24]:

data


# In[25]:

arr = np.empty((8,4))


# In[26]:

arr


# In[27]:

for i in range(8):
    arr[i, :] = i


# In[28]:

arr


# In[30]:

for i in range(8):
    arr[i] = i + 1


# In[31]:

arr


# In[32]:

arr[[4,3,0,6]]


# In[33]:

arr[[-3,-5,-7]]


# In[34]:

arr = np.arange(32).reshape((8,4))


# In[35]:

arr


# In[36]:

arr[[1,5,7,2],[0,3,1,2]]


# In[37]:

arr[[1,5,7,2]][:,[0,3,1,2]]


# In[38]:

arr[np.ix_([1,5,7,2],[0,3,1,2])]


# In[39]:

arr = np.arange(35).reshape((5,7))


# In[40]:

arr


# In[41]:

arr.T


# In[42]:

arr = randn(6,3)


# In[43]:

arr


# In[44]:

np.dot(arr.T, arr)


# In[45]:

arr = np.arange(16).reshape((2,2,4))


# In[46]:

arr


# In[47]:

arr.swapaxes(1,2)


# In[48]:

arr = np.arange(10)


# In[49]:

arr


# In[52]:

np.sqrt(arr)


# In[53]:

np.exp(arr)


# In[54]:

x = randn(8)


# In[55]:

x


# In[56]:

y = randn(8)


# In[57]:

y


# In[58]:

np.maximum(x,y)


# In[59]:

arr = randn(7)*5


# In[60]:

np.modf(arr)


# In[61]:

points = np.arange(-5,5,0.01)


# In[62]:

xs, ys = np.meshgrid(points, points)


# In[63]:

import matplotlib.pyplot as plt


# In[68]:

z = np.sqrt(xs**2 + ys**2)


# In[70]:

plt.imshow(z, cmap = plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()


# In[71]:

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])


# In[72]:

yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])


# In[73]:

cond = np.array([True, False, True, True, False])


# In[74]:

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]


# In[75]:

result


# In[77]:

result =  np.where(cond, xarr, yarr)


# In[78]:

result


# In[79]:

arr = randn(4, 4)


# In[80]:

arr


# In[82]:

np.where(arr > 0, 2, -2)


# In[83]:

np.where(arr >0, 2, arr)


# In[84]:

arr = randn(5, 4)


# In[85]:

arr


# In[86]:

arr.mean()


# In[87]:

np.mean(arr)


# In[88]:

arr.sum()


# In[89]:

arr.mean(axis = 1)


# In[90]:

np.mean(arr[0])


# In[91]:

arr.sum(0)


# In[92]:

np.sum(arr[:, 0])


# In[94]:

arr = randn(100)


# In[95]:

(arr>0).sum()


# In[96]:

bools = np.array([False, False, True, False])


# In[97]:

bools.any()


# In[98]:

bools.all()


# In[99]:

arr =  randn(8)


# In[100]:

arr


# In[101]:

arr.sort()


# In[102]:

arr


# In[103]:

arr = randn(5, 3)


# In[104]:

arr


# In[105]:

arr.sort(1)


# In[106]:

arr


# In[107]:

large_arr = randn(1000)


# In[108]:

large_arr.sort()


# In[109]:

large_arr[int(0.05 * len(large_arr))]


# In[110]:

len(large_arr)


# In[111]:

large_arr.shape


# In[112]:

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])


# In[113]:

np.unique(names)


# In[114]:

sorted(set(names))


# In[115]:

ints = np.array([3,3,3,2.2,1,1,4,4])


# In[116]:

np.unique(ints)


# In[117]:

len(np.unique(ints))


# In[118]:

np.unique(ints).shape


# In[119]:

values = np.array([6,0,0,3,2,5,6])


# In[120]:

np.in1d(values, [2,3,6])


# In[121]:

arr = np.arange(10)


# In[122]:

np.save('some_array', arr)


# In[123]:

np.load('some_array.npy')


# In[124]:

np.savez('array_achive.npz', a = arr, b = arr)


# In[125]:

arch = np.load('array_achive.npz')


# In[126]:

arch['b']


# In[ ]:



