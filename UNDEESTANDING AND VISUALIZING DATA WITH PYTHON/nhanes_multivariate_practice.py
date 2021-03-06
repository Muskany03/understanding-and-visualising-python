
# coding: utf-8

# # Practice notebook for multivariate analysis using NHANES data
# 
# This notebook will give you the opportunity to perform some multivariate analyses on your own using the NHANES study data.  These analyses are similar to what was done in the week 3 NHANES case study notebook.
# 
# You can enter your code into the cells that say "enter your code here", and you can type responses to the questions into the cells that say "Type Markdown and Latex".
# 
# Note that most of the code that you will need to write below is very similar to code that appears in the case study notebook.  You will need to edit code from that notebook in small ways to adapt it to the prompts below.
# 
# To get started, we will use the same module imports and read the data in the same way as we did in the case study:

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")
da.columns


# ## Question 1
# 
# Make a scatterplot showing the relationship between the first and second measurements of diastolic blood pressure ([BPXDI1](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXDI1) and [BPXDI2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXDI2)).  Also obtain the 4x4 matrix of correlation coefficients among the first two systolic and the first two diastolic blood pressure measures.

# In[2]:


# enter your code here
sns.regplot(x="BPXDI1", y="BPXDI2", data=da, fit_reg=False, scatter_kws={"alpha": 0.2})


# In[9]:


print(da.loc [:,["BPXDI1", "BPXDI2"]].dropna().corr())
print(da.loc[:,["BPXSY1", "BPXSY2"]].dropna().corr())


# __Q1a.__ How does the correlation between repeated measurements of diastolic blood pressure relate to the correlation between repeated measurements of systolic blood pressure?

# __Q2a.__ Are the second systolic and second diastolic blood pressure measure more correlated or less correlated than the first systolic and first diastolic blood pressure measure?

# ## Question 2
# 
# Construct a grid of scatterplots between the first systolic and the first diastolic blood pressure measurement.  Stratify the plots by gender (rows) and by race/ethnicity groups (columns).

# In[11]:


# insert your code here
_ = sns.FacetGrid(da, col="RIDRETH1",  row="RIAGENDR").map(plt.scatter, "BPXDI1", "BPXSY1", alpha=0.5).add_legend()


# __Q3a.__ Comment on the extent to which these two blood pressure variables are correlated to different degrees in different demographic subgroups.

# ## Question 3
# 
# Use "violin plots" to compare the distributions of ages within groups defined by gender and educational attainment.

# In[15]:


# insert your code here
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 
                                       7: "Refused", 9: "Don't know"})
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"}) 
db = da.loc[(da.DMDEDUC2x != "Don't know"), :]
plt.figure(figsize=(12, 4))
a = sns.violinplot(db.DMDEDUC2x, db.RIDAGEYR,db.RIAGENDRx)


# __Q4a.__ Comment on any evident differences among the age distributions in the different demographic groups.

# ## Question 4
# 
# Use violin plots to compare the distributions of BMI within a series of 10-year age bands.  Also stratify these plots by gender.

# In[23]:


# insert your code here
plt.figure(figsize=(12, 4))
a = sns.violinplot(db.BMXWT, db.BMXHT, db.BMXBMI, db.BMXLEG,db.BMXARML, db.BMXARMC,db.BMXWAIST, db.RIDAGEYR,db.RIAGENDRx)


# __Q5a.__ Comment on the trends in BMI across the demographic groups.

# ## Question 5
# 
# Construct a frequency table for the joint distribution of ethnicity groups ([RIDRETH1](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIDRETH1)) and health-insurance status ([HIQ210](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HIQ_I.htm#HIQ210)).  Normalize the results so that the values within each ethnic group are proportions that sum to 1.

# In[24]:


# insert your code here
x = pd.crosstab(db.RIDRETH1, da.HIQ210)
x


# In[26]:


x.apply(lambda z: z/z.sum(), axis=0)


# __Q6a.__ Which ethnic group has the highest rate of being uninsured in the past year?
