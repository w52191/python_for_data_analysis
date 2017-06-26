
# coding: utf-8

# In[124]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt


# In[107]:

fig = plt.figure();ax1 = fig.add_subplot(2, 2, 1)


# In[106]:

ax1 = fig.add_subplot(2, 2, 1)


# In[87]:

ax2 = fig.add_subplot(2, 2, 2)


# In[88]:

ax3 = fig.add_subplot(2, 2, 3)


# In[89]:

plt.show()


# In[90]:

from numpy.random import randn


# In[91]:

plt.plot(randn(50).cumsum(), 'k--')


# In[34]:

plt.show()


# In[44]:

_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)


# In[45]:

import numpy as np
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))


# In[46]:

plt.show()


# In[51]:

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)


# In[48]:

plt.show()


# In[52]:

plt.subplots_adjust(wspace=0, hspace=0)


# In[53]:

plt.show()


# In[54]:

plt.plot(randn(30).cumsum(), 'ko--')


# In[55]:

plt.show()


# In[57]:

plt.plot(randn(30).cumsum(), color='k', linestyle='dashed', marker='o')


# In[58]:

plt.show()


# In[99]:

data = randn(30).cumsum()


# In[100]:

plt.plot(data, 'k--', label='Default')


# In[61]:

plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')


# In[62]:

plt.legend(loc='best')


# In[63]:

plt.show()


# In[72]:

fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)


# In[73]:

ax.plot(randn(1000).cumsum())


# In[66]:

plt.show()


# In[74]:

ticks = ax.set_xticks([0, 250, 500, 750, 1000])


# In[75]:

labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
rotation=30, fontsize='small')


# In[76]:

ax.set_title('My first matplotlib plot')


# In[77]:

ax.set_xlabel('Stages')


# In[78]:

plt.show()


# In[120]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='_nolegend_')
ax.legend(loc='best')
ax.text(0, 40, 'Hello world!',
family='monospace', fontsize=10)


# In[123]:

from datetime import datetime
import pandas as pd
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
data = pd.read_csv('ch08/spx.csv', index_col=0, parse_dates=True)
spx = data['SPX']
spx.plot(ax=ax, style='k-')
crisis_data = [
(datetime(2007, 10, 11), 'Peak of bull market'),
(datetime(2008, 3, 12), 'Bear Stearns Fails'),
(datetime(2008, 9, 15), 'Lehman Bankruptcy')
]
for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 50),
        xytext=(date, spx.asof(date) + 200),
        arrowprops=dict(facecolor='black'),
        horizontalalignment='left', verticalalignment='top')
# Zoom in on 2007-2010
ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title('Important dates in 2008-2009 financial crisis')


# In[126]:

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)


# In[ ]:



