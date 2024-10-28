#!/usr/bin/env python
# coding: utf-8

# In[3]:


import duckdb
import psycopg2


# In[6]:


# Connect to DuckDB
conn = duckdb.connect('exercise.db')


# In[9]:


conn.execute("""
INSTALL postgres;
LOAD postgres;
ATTACH 'dbname=postgres user=postgres password=your_password host=127.0.0.1' AS db (TYPE POSTGRES, SCHEMA 'public');
""")


# In[11]:


#insert country table as reference 
conn.execute("""
INSERT INTO db.country 
SELECT 
*
FROM country
""")


# In[13]:


#insert restaurants as reference 
conn.execute("""
INSERT INTO db.restaurants 
SELECT 
*
FROM resturants
""")


# In[24]:


#insert restaurants_details as reference 
conn.execute("""
INSERT INTO db.resturants_details 
SELECT 
    has_online_delivery
    ,photos_url
    ,url
    ,price_range
    ,apikey
    ,rating_text
    ,rating_color
    ,votes
    ,aggregate_rating
    ,res_id
    ,name
    ,has_table_booking
    ,is_delivering_now
    ,deeplink
    ,menu_url
    ,average_cost_for_two
    ,switch_to_order_menu
    ,cuisines
    ,latitude
    ,address
    ,city
    ,country_id
    ,locality_verbose
    ,city_id
    ,zipcode
    ,longitude
    ,locality
    ,featured_image
    ,currency
    ,id
    ,thumb
    ,events_url
    ,book_url
    ,order_deeplink
    ,order_url
FROM resturants_details
where res_id in (select "Restaurant ID" from resturants)
""")


# In[25]:


conn.close()


# In[ ]:




