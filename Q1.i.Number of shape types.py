#!/usr/bin/env python
# coding: utf-8

# ##Required Libraries

# In[1]:


import json
from pandas import DataFrame
from collections import Counter 


# ##Reading the Json File

# In[2]:


with open('sample-json.json') as f:
    data = json.load(f)


# ##Converting the json file to a data frame so as to read the data in the file and see the variables in a proper manner as it would have seemed gibberish normally

# In[3]:


df = DataFrame(data)
df.head()

##Creating lists to be able to order the unique elements or to catch the data in an ordered sequence as the Json dataset has the data given in unordered manner.
# In[4]:


label = list()
shape = list()
taggable_image = list()
points = list()
index = list()


# ##Creating a for loop to create an iteration for the count of images and appending the values of the varaibles to the list

# In[5]:


for dt in data:
    taggable_image.append(dt['taggable image'])


# In[6]:


for t in taggable_image:
    for i in t:
        label.append(i['tags']['label'])
        shape.append(i['type'])
        points.append(i['points'])
        index.append(i['index'])


# ##Creating a function to tally the unique shapes(creating a set of the unique shape from the list) and its count(calclulating the length of the set 's')

# In[7]:


def number_unique_shapes(s):
    return f"Unique Shapes {list(set(s))}. Number: {len(list(set(s)))}"


# In[8]:


if __name__ == '__main__':
    print(number_unique_shapes(shape))


# In[ ]:




