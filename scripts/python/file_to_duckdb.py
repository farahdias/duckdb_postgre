#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the requirement
import duckdb
import glob
import pandas as pd


# In[2]:


#specify the path to the file
path_data = 'path to directory'


# In[3]:


# Connect to an in-memory DuckDB database
conn = duckdb.connect("exercise.db")


# In[4]:


#load the all JSON Files
conn.execute("""
CREATE TABLE resturants_details as
SELECT 
unnest(restaurants, recursive := true)
FROM read_json_auto('{}*.json')
where 
 results_found is not null
""".format(path_data))


# In[5]:


#load the CSV Files
conn.execute("""
CREATE TABLE resturants as
SELECT 
*
FROM read_csv('{}*.csv', ignore_errors=true)
""".format(path_data))


# In[6]:


conn.execute("""
INSTALL spatial;
LOAD spatial;
CREATE TABLE country as
SELECT 
*
FROM st_read('{}Country-Code.xlsx')
""".format(path_data))


# In[7]:


# Close the connection
conn.close()


# In[ ]:




