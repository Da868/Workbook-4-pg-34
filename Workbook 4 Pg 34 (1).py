#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[20]:


import numpy as np
df['Pass/Fail'] = np.where(df['grade']<=80,'Failing','Passing')
df.head()


# In[18]:


df.groupby(['fname','lname','grade']).pass/fail.agg(lambda x: 'Pass' if x.ge(79.99).all() else 'fail' ).reset_index(name='Pass/Fail')


# In[ ]:




