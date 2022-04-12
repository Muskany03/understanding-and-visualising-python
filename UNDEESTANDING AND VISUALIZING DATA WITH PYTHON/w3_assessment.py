
# coding: utf-8

# In this assignment we'll ask you to plot multiple variables.   
# 
# You will use what you find in this assignment to answer the questions in the quiz that follows. It may be useful to keep this notebook side-by-side with this week's quiz on your screen.

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)

path = "Cartwheeldata.csv"


# In[3]:


# First, you must import the cartwheel data from the path given above
df = pd.read_csv("Cartwheeldata.csv") # using pandas, read in the csv data found at the url defined by 'path'


# In[4]:


# Next, look at the 'head' of our DataFrame 'df'. 
df.head()


# If you can't remember a function, open a previous notebook or video as a reference, or use your favorite search engine to look for a solution.

# ## Scatter plots

# First, let's looks at two variables that we expect to have a strong relationship, 'Height' and 'Wingspan'.

# In[5]:


# Make a Seaborn scatter plot with x = height and y = wingspan using sns.scatterplot(x, y)
sns.scatterplot( x = "Height",y = "Wingspan",data=df,hue=df['Gender'])


# How would you describe the relationship between 'Height' and 'Wingspan'?   
# Questions you can ask:
# * Is it linear?
# * Are there outliers?
# * Are their ranges similar or different?  
# 
# How else could you describe the relationship?

# Now let's look at two variables that we don't yet assume have a strong relationship, 'Wingspan' and 'CWDistance'

# In[8]:


# Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance
sns.scatterplot( x = "Wingspan",y ="CWDistance" ,data=df)


# How would you describe the relationship between 'Wingspan' and 'CWDistance'?   
# * Is it linear?
# * Are there outliers?
# * Are their ranges similar or different?  
# 
# How else could you describe the relationship?

# Let makes the same plot as above, but now include 'Gender' as the color scheme by including the argument
# ```
# hue=df['Gender']
# ```
# in the Seaborn function

# In[9]:


# Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance, and hue = gender
sns.scatterplot( x = "Wingspan",y ="CWDistance" ,data=df,hue=df['Gender'])


# Does does this new information on the plot change your interpretation of the relationship between 'Wingspan' and 'CWDistance'?

# ## Barcharts
# Now lets plot barplots of 'Glasses'

# In[10]:


# Make a Seaborn barplot with x = glasses and y = cartwheel distance
sns.barplot( x = "CWDistance",y = "Glasses",data=df)


# What can you say about the relationship of 'Glasses' and 'CWDistance'?

# In[11]:


# Make the same Seaborn boxplot as above, but include gender for the hue argument
sns.barplot( x = "CWDistance",y = "Glasses",data=df,hue=df['Gender'])


# In[13]:



df.boxplot(column=["Wingspan","CWDistance"])


# How does this new plot change your interpretation about the relationship of 'Glasses' and 'CWDistance'?
