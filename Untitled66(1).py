#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


data =pd.read_csv('apple product price list from 26 countries.xls')
data


# In[3]:


data.info()


# In[4]:


data.describe()


# In[5]:


data.isna().sum()


# In[6]:


data1=data.copy()


# In[24]:


data1.head(12)


# In[11]:


data1.drop(['country_code'],inplace=True,axis=1)


# In[12]:


data1


# In[13]:


data['scraped_date']=pd.to_datetime(data1['scraped_date'],format='%Y-%m-%d')


# In[14]:


data1


# In[19]:


data1['income group'].value_counts()


# In[20]:


aus_hi=data1.loc[(data1['income group']=='High income')&(data1['country']=='Australia')]
aus_hi


# In[23]:


us_li=data1.loc[(data1['income group']=='Lower middle income')&(data1['country']=='United States')]


# In[29]:


data1.loc[(data1['model']=='iPhone 13')&(data1['country']=='Canada')]


# In[30]:


data1.sort_values(by=['price'],ascending=False)
data1=data1.head(10)
print(data['model'])


# In[32]:


data1.style.background_gradient(cmap='cubehelix')


# In[41]:


maxx=data1.groupby('country').max()['price']
maxx


# In[43]:


minn=data1.groupby('country').min()['price']
minn


# In[50]:



plt.title('price vs income group')
plt.xlabel('income')
plt.ylabel('price')
plt.bar(data1['income group'],data1['price'])
plt.show()


# In[ ]:




