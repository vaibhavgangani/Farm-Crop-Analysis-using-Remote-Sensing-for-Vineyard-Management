#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[3]:


#Importing Earth Engine
import ee


# In[4]:


#Importing geemap - a python based library for GEE
import geemap


# In[5]:


#Giving Authorization and plotting basemap
Map=geemap.Map()
Map


# In[ ]:





# In[ ]:





# In[6]:


Map


# In[63]:


#defining Center
Map.setCenter(73.79501667,20.26367500,16)


# In[ ]:





# In[8]:





# In[9]:





# In[66]:


#Importing Shapefile
field1=ee.FeatureCollection("users/rvdigimarketing/K26")


# In[74]:


#Importing Satellite Data - Sentinel-2A 
data=ee.ImageCollection("COPERNICUS/S2_SR").filterBounds(field1) ;


# In[106]:


#Filtering Bands and Dates
image=ee.Image(data.filterDate("2019-01-12","2020-03-25").sort("CLOUD_COVERAGE_ASSESSMENT").first().clip(field1));


# In[ ]:





# In[107]:


#NDVI function
ndvi=image.expression(
"(NIR - RED) / (NIR + RED)",
{"NIR":image.select("B8"),
"RED":image.select("B4")});


# In[108]:


#Display Parameters
display={
    "min":0,
    "max":1,
    "palette":[ '#10d22c','#ffff52', '#0000ff']
}


# In[109]:


#Adding Final ouput to Map
Map.addLayer(ndvi,display);

Map


# In[115]:


geemap.ee_export_image_to_drive(image, description='sentinel_NDVI', folder='export', region=field1, scale=10)

