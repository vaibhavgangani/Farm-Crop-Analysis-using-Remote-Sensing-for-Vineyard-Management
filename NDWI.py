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


# In[37]:


#Importing Shapefile
field1=ee.FeatureCollection("users/rvdigimarketing/K15")


# In[38]:


#Importing Satellite Data - Sentinel-2A 
data=ee.ImageCollection("COPERNICUS/S2_SR").filterBounds(field1) ;


# In[39]:


#Filtering Bands and Dates
image=ee.Image(data.filterDate("2019-01-12","2020-03-25").sort("CLOUD_COVERAGE_ASSESSMENT").first().clip(field1));


# In[47]:


#NDWI function
ndwi=image.expression(
"(NIR - SWIR) / (NIR + SWIR)",
{"NIR":image.select("B8"),
"SWIR":image.select("B11")});


# In[48]:


#Display Parameters
display={
    "min":0,
    "max":1,
    "palette":[ 'green','yellow', 'orange', 'blue', 'red']
}


# In[49]:


#Adding Final ouput to Map
Map.addLayer(ndwi,display);

Map


# In[15]:


geemap.ee_export_image_to_drive(image, description='sentinel_NDWI', folder='export', region=field1, scale=10)

