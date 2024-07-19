#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url = 'https://www.flipkart.com/'  # Replace with the URL of the webpage you want to scrape


# In[3]:


response = requests.get(url)


# In[4]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[5]:


links = soup.find_all('a')
for link in links:
    print(link.get('href'))


# In[ ]:




