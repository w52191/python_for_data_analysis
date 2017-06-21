
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


# In[2]:

obj = Series([4.5,7.2,-5.3,3.6], index =['b','d','a','c'])


# In[3]:

obj


# In[4]:

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])


# In[5]:

obj2


# In[6]:

obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value = 0)


# In[7]:

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])


# In[8]:

obj3.reindex(range(6), method = 'ffill')


# In[10]:

import numpy as np
frame = DataFrame(np.arange(9).reshape(3, 3), index = ['a', 'b', 'c'], columns = ['Ohio', 'Texes', 'California'])


# In[11]:

frame


# In[14]:

frame2 = frame.reindex(['a', 'b', 'c', 'd'])


# In[15]:

frame2


# In[16]:

states = ['Texas', 'Utah', 'California']


# In[17]:

frame.reindex(columns=states)


# In[18]:

frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill',
columns=states)


# In[19]:

frame.ix[['a', 'b', 'c', 'd'], states]


# In[24]:

obj = Series(np.arange(5.0), index = ['a', 'b', 'c', 'd', 'e'])


# In[25]:

obj


# In[26]:

new_obj = obj.drop('c')


# In[27]:

new_obj


# In[29]:

obj.drop(['d','c'])


# In[35]:

data = DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])


# In[36]:

data


# In[37]:

data.drop(['Colorado', 'Ohio'])


# In[39]:

data.drop('two', axis = 1)


# In[40]:

data.drop(['two', 'four'], axis=1)


# In[41]:

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])


# In[42]:

obj


# In[43]:

obj['b']


# In[44]:

obj[1]


# In[45]:

obj[2:4]


# In[46]:

obj[['b', 'a', 'd']]


# In[47]:

obj[[1,3]]


# In[48]:

obj[obj<2]


# In[49]:

obj['b':'c'] = 5


# In[50]:

obj


# In[51]:

obj[['b','c']] = 8


# In[52]:

obj


# In[53]:

data


# In[54]:

data[:2]


# In[55]:

data[data['three'] > 5]


# In[56]:

data < 5


# In[57]:

data[data < 5] = 0


# In[58]:

data


# In[59]:

data.ix['Colorado',['three','two']]


# In[60]:

data.ix[['Colorado', 'Utah'], [3, 0, 1]]


# In[61]:

data.ix[2]


# In[62]:

data.ix[:'Utah', 'two']


# In[63]:

data.ix[data.three > 5, :3]


# In[64]:

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])


# In[65]:

s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])


# In[66]:

s1


# In[67]:

s2


# In[68]:

s1 + s2


# In[69]:

df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
index=['Ohio', 'Texas', 'Colorado'])


# In[70]:

df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])


# In[71]:

df1


# In[72]:

df2


# In[73]:

df1 + df2


# In[76]:

list('bcd_1')


# In[77]:

df1.add(df2, fill_value = 0)


# In[78]:

df1.reindex(columns=df2.columns, fill_value=0)


# In[79]:

arr = np.arange(12.).reshape((3, 4))


# In[80]:

arr-arr[0]


# In[81]:

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])


# In[82]:

series = frame.ix[0]


# In[83]:

frame - series


# In[85]:

series2 = Series(range(3), index=['b', 'e', 'f'])


# In[86]:

frame + series2


# In[87]:

series3 = frame['d']


# In[88]:

frame.sub(series3)


# In[89]:

frame.sub(series3, axis=0)


# In[91]:

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])


# In[92]:

frame


# In[93]:

np.abs(frame)


# In[94]:

f = lambda x: x.max() - x.min()


# In[95]:

frame.apply(f)


# In[96]:

frame.apply(f, axis = 1)


# In[97]:

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])


# In[98]:

frame.apply(f)


# In[99]:

format = lambda x: '% .2f' %x


# In[100]:

frame.applymap(format)


# In[102]:

frame['e'].map(format)


# In[103]:

test = frame['e']


# In[104]:

test


# In[105]:

test[0] = 7


# In[106]:

test


# In[107]:

frame


# In[111]:

test1 = frame['e'].copy()


# In[112]:

test1


# In[113]:

test1[0] = 5


# In[114]:

frame


# In[115]:

test1


# In[116]:

obj = Series(range(4), index=['d', 'a', 'b', 'c'])


# In[117]:

obj.sort_index()


# In[118]:

frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
columns=['d', 'a', 'b', 'c'])


# In[119]:

frame.sort_index(axis=1)


# In[120]:

frame.sort_index(axis=1, ascending=False)


# In[121]:

obj.order()


# In[122]:

obj.sort_values()


# In[123]:

frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})


# In[124]:

frame


# In[125]:

frame.sort_index(by='b')


# In[126]:

frame.sort_values(by = 'b')


# In[127]:

frame.sort_index(by=['a', 'b'])


# In[128]:

obj = Series([7, -5, 7, 4, 2, 0, 4])


# In[129]:

obj.rank()


# In[130]:

obj.rank(method='first')


# In[131]:

obj.rank(ascending=False, method='max')


# In[132]:

frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
'c': [-2, 5, 8, -2.5]})


# In[133]:

frame.rank(axis=1)


# In[134]:

obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])


# In[135]:

obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])


# In[136]:

obj.index.is_unique


# In[137]:

obj['a']


# In[138]:

df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])


# In[139]:

df.ix['b']


# In[140]:

df = DataFrame([[1.4, np.nan], [7.1, -4.5],
[np.nan, np.nan], [0.75, -1.3]],
index=['a', 'b', 'c', 'd'],
columns=['one', 'two'])


# In[141]:

df.sum()


# In[142]:

df.sum(axis=1)


# In[143]:

df


# In[144]:

df.mean(axis=1, skipna=False)


# In[145]:

df.sum(axis=1, skipna=False)


# In[146]:

df.idxmax()


# In[147]:

df.cumsum()


# In[148]:

df.describe()


# In[149]:

obj = Series(['a', 'a', 'b', 'c'] * 4)


# In[150]:

obj


# In[151]:

obj.describe()


# In[152]:

import pandas.io.data as web


# In[153]:

obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])


# In[154]:

uniques = obj.unique()


# In[155]:

uniques


# In[156]:

obj.value_counts()


# In[157]:

pd.value_counts(obj.values, sort=False)


# In[158]:

uniques.sort()


# In[159]:

uniques


# In[160]:

mask =obj.isin(['b','c'])


# In[161]:

mask


# In[162]:

obj[mask]


# In[163]:

data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
'Qu2': [2, 3, 1, 2, 3],
'Qu3': [1, 5, 2, 4, 4]})


# In[164]:

result = data.apply(pd.value_counts).fillna(0)


# In[165]:

result


# In[166]:

string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])


# In[167]:

string_data


# In[168]:

string_data.isnull()


# In[169]:

string_data[0] = None


# In[170]:

string_data.isnull()


# In[171]:

from numpy import nan as NA


# In[172]:

data = Series([1, NA, 3.5, NA, 7])


# In[173]:

data


# In[174]:

data.drop(data[0])


# In[175]:

data.drop(2)


# In[176]:

data.dropna()


# In[177]:

data[data.notnull()]


# In[180]:

data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
[NA, NA, NA], [NA, 6.5, 3.]])


# In[179]:

ata


# In[181]:

cleaned = data.dropna()


# In[182]:

cleaned


# In[183]:

data.dropna(how = 'all')


# In[184]:

data[4] = NA


# In[185]:

data


# In[186]:

data[2]


# In[187]:

data.dropna(axis=1, how='all')


# In[188]:

data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
[NA, NA, NA], [NA, 6.5, 3.]])


# In[189]:

data


# In[190]:

data[2]


# In[191]:

df = DataFrame(np.random.randn(7, 3))


# In[192]:

df


# In[193]:

df.ix[:4, 1] = NA; df.ix[:2, 2] = NA


# In[194]:

df


# In[195]:

df[:4]


# In[196]:

df.dropna(thresh=3)


# In[197]:

df.dropna(thresh=2)


# In[198]:

df.fillna(0)


# In[199]:

df.fillna({1: 0.5, 3: -1})


# In[200]:

df.fillna({1: 0.5, 3: -1})


# In[201]:

df.fillna({1: 0.5, 2: -1})


# In[202]:

data = Series(np.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])


# In[203]:

data


# In[204]:

data.index


# In[205]:

data['b':'c'] 


# In[206]:

data[:, 2]


# In[207]:

data.unstack()


# In[208]:

data.unstack().stack()


# In[209]:

frame = DataFrame(np.arange(12).reshape((4, 3)),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=[['Ohio', 'Ohio', 'Colorado'],
['Green', 'Red', 'Green']])


# In[210]:

frame


# In[211]:

frame.index.names = ['key1', 'key2']


# In[212]:

frame.columns.names = ['state', 'color']


# In[213]:

frame


# In[214]:

MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
names=['state', 'color'])


# In[215]:

frame.swaplevel('key1', 'key2')


# In[216]:

frame.sortlevel(1)


# In[217]:

frame


# In[218]:

frame.swaplevel(0, 1).sortlevel(0)


# In[219]:

frame.sum(level='key2')


# In[220]:

frame.sum(level='color', axis=1)


# In[221]:

frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
'd': [0, 1, 2, 0, 1, 2, 3]})


# In[222]:

frame


# In[223]:

frame2 = frame.set_index(['c', 'd'])


# In[224]:

frame2


# In[225]:

frame.set_index(['c', 'd'], drop=False)


# In[226]:

frame2.reset_index()


# In[227]:

ser = Series(np.arange(3.))


# In[229]:

ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])


# In[230]:

ser2


# In[231]:

ser3 = Series(range(3), index=[-5, 1, 3])


# In[232]:

ser3


# In[233]:

ser3.iget_value(2)


# In[235]:

frame = DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])


# In[236]:

frame


# In[237]:

frame.irow(0)


# In[ ]:



