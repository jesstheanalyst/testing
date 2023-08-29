#!/usr/bin/env python
# coding: utf-8

# In[ ]:


https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128#:~:text=For%20example%2C%20haversine(%CE%B8),longitude%20of%20the%20two%20points.


# In[1]:


import math


# In[2]:


"Calculate distance using the Haversine Formula"


def haversine(coord1: object, coord2: object):

    # Coordinates in decimal degrees (e.g. 2.89078, 12.79797)
    -84.386330, 33.7488 == coord1
    -76.609383, 39.299236 == coord2

R = 6371000  # radius of Earth in meters
phi_1 = math.radians(33.7488)
phi_2 = math.radians(39.299236)

delta_phi = math.radians(39.299236 - 33.7488)
delta_lambda = math.radians(-76.609383 - -84.386330)

a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

meters = R * c  # output distance in meters
km = meters / 1000.0  # output distance in kilometers

meters = round(meters, 3)
km = round(km, 3)


print(f"Distance: {meters} m")
print(f"Distance: {km} km")


# In[ ]:




