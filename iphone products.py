#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().system('pip install plotly')
import plotly.express as px
import plotly.graph_object as go


# In[6]:


data= pd.read_csv('apple_products.xls')
data.head()


# In[5]:


data.info()


# In[7]:


data.describe()


# In[11]:


highst_rated=data.sort_values(by=['Star Rating'],ascending=False)
highst_rated=highst_rated.head(10)
highst_rated['Product Name']


# In[ ]:


data['Product Name'].unique()


# In[12]:


n_o_rating=data.sort_values(by=['Number Of Ratings'],ascending=False)
n_o_rating=n_o_rating.head(10)
n_o_rating['Product Name']


# In[18]:


data['Product Name'].value_counts()


# In[ ]:


iphone=highst_rated['Product Name'].value_counts()
label=iphone.index()
counts=highst_rated['Number Of Ratings']

figure=px.bar(highst_rated,x=label,y=counts)
figure.show()


# In[2]:


iphone=highst_rated['Product Name'].value_counts()
label=iphone.index()
counts=highst_rated['Number Of Reviews']
figure=px.bar(highst_rated,x=label,y=counts)
figure.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




