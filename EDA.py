#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

file_path = 'E:\INNOMATICS\data.xlsx'
df = pd.read_excel(file_path)


# In[4]:


print(df.head())


# In[6]:


print(df.isnull().sum())


# In[7]:


print(df.head())
print(df.info())
print(df.describe())


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


plt.figure(figsize=(8, 6))
sns.histplot(df['Salary'], bins=20, kde=True)
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()


# In[14]:


plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Salary', data=df)
plt.title('Box plot of Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.show()


# In[15]:


plt.figure(figsize=(8, 6))
sns.scatterplot(x='10percentage', y='Salary', data=df)
plt.title('Scatter plot of 10percentage vs Salary')
plt.xlabel('10percentage')
plt.ylabel('Salary')
plt.show()


# In[18]:


numeric_data = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(12, 10))
sns.heatmap(numeric_data.corr()[['Salary']], annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap with Salary')
plt.show()


# In[22]:


sns.pairplot(df, vars=['Salary', 'English', 'Logical', 'Quant', 'Domain','ComputerProgramming','ElectronicsAndSemicon','MechanicalEngg'])
plt.show()


# In[ ]:





# In[ ]:




