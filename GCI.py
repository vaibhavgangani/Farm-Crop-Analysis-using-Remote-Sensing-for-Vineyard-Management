#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imprting Earth Engine Library
import ee


# In[2]:


#Importing Geemap Python based library
import geemap


# In[3]:


#Giving Authorization and plotting basemap
Map=geemap.Map()
Map


# In[4]:


#defining Center
Map.setCenter(73.79501667,20.26367500,16)


# In[20]:


#Importing Shapefile
field1=ee.FeatureCollection("users/rvdigimarketing/K26")


# In[34]:


#Importing Satellite Data - Sentinel
data=ee.ImageCollection("COPERNICUS/S2").filterBounds(field1) ;


# In[35]:


#Filtering Bands and Dates
image=ee.Image(data.filterDate("2019-01-12","2020-03-25").sort("CLOUD_COVERAGE_ASSESSMENT").first().clip(field1));


# In[36]:


#GCI function
gci=image.expression(
"((NIR)/(Green)-1)",
{"NIR":image.select("B8"),
"Green":image.select("B3")});


# In[37]:


#Display Parameters
display={
    "min":0,
    "max":1,
    "palette":['orange','yellow','green', 'blue']
}


# In[38]:


#Adding Final ouput to Map
Map.addLayer(gci,display);

Map

