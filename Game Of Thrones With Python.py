#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


n1 = np.array([5,7,8,9,0])
n1


# In[4]:


np.array([[1,2,3,4,5],[5,4,3,2,1]])


# In[5]:


#numpy.zeros


# In[7]:


n1 = np.zeros((4,5))
n1


# In[8]:


n2 = np.zeros((6,3))
n2


# In[9]:


#np.full


# In[11]:


n3 = np.full((9,9),1)
n3


# In[12]:


#np.arange


# In[15]:


np.arange(20,51,10)


# In[16]:


#pandas


# In[17]:


import pandas as pd


# In[19]:


s1=pd.Series([1,2,3,4,5])
s1


# In[20]:


type(s1)


# In[22]:


s1=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
s1


# In[23]:


s1 = pd.Series([1,2,3,4,5,6,7,8,9,])
s1


# In[24]:


s1[6]


# In[25]:


s1[:5]


# In[26]:


# Data-Frame


# In[29]:


pd.DataFrame({"Name":["Julia","Anne","Jennifer"],"Marks":[50,60,70]})


# In[30]:


#Visualization


# In[31]:


import seaborn as sns
from matplotlib import pyplot as plt


# In[33]:


fmri=sns.load_dataset("fmri")
fmri.head()


# In[34]:


sns.lineplot(x="timepoint",y="signal",data=fmri)
plt.show()


# In[35]:


import pandas as pd
import numpy as p


# In[40]:


battle = pd.read_csv("C:/Users/azobe/Downloads/Data_TP/battles.csv")


# In[41]:


battle.head()


# In[42]:


battle.shape


# In[44]:


battle.rename(columns={'attacker_1':'primary_attacker'},inplace=True)
battle.head()


# In[45]:


battle.rename(columns={'defender_1':'primary_defender'},inplace=True)
battle.head()


# In[46]:


battle['attacker_king'].value_counts()


# In[47]:


battle['location'].value_counts()


# In[48]:


import seaborn as sns
from matplotlib import pyplot as plt


# In[49]:


sns.set(rc={'figure.figsize':(13,5)})
sns.barplot(x='attacker_king',y='attacker_size',data = battle)
plt.show()


# In[50]:


sns.set(rc={'figure.figsize':(13,5)})
sns.barplot(x='defender_king',y='defender_size',data = battle)
plt.show()


# In[51]:


sns.countplot(x=battle['attacker_king'],hue=battle['battle_type'])
plt.show()


# In[53]:


death=pd.read_csv('C:/Users/azobe/Downloads/Data_TP/character-deaths.csv')
death.head()


# In[54]:


death.shape


# In[55]:


death['Gender'].value_counts()


# In[56]:


death['Nobility'].value_counts()


# In[57]:


sns.countplot(death['Death Year'])
plt.show()


# In[58]:


sns.set(rc={'figure.figsize':(30,10)})
sns.countplot(death['Allegiances'])
plt.show()


# ## Thanks
