#!/usr/bin/env python
# coding: utf-8

# ##Required Libraries

# In[1]:


import json
from pandas import DataFrame
from collections import Counter 
from PIL import Image, ImageDraw, ImageFont
from itertools import chain


# ##Reading the JSON file

# In[2]:


with open('sample-json.json') as f:
    data = json.load(f)


# In[3]:


df = DataFrame(data)
df.head()


# ##Creating lists to be able to order the unique elements or to catch the data in an ordered sequence as the Json dataset has the data given in unordered manner.

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


# ##create a function that combines the shapes and its label to a zip so as to iterate or counter the count to the shape so that it can be tally'd

# In[7]:


def frequency_of_shapes(l,s):
    cntr = Counter(list(zip(shape,label)))
    for x, y in cntr.items():
        print(f"Shape/Label: {x}, Count:{y}")


# ##Combined the dictionary using the key-value pair that is unordered, shape and value to create a separate Jpeg or png to visualize it

# In[8]:


comb_dict = dict()
comb_list = list()


# In[9]:


for g in range(len(shape)):
    comb_dict[shape[g]] = points[g] 
    comb_list.append(comb_dict)


# ##Created a folder "Question1 Images" in the local drive where the separate images can be saved then created the below function which take the three uniques shapes and create an image with dimension 3840, 2160

# In[15]:


def visualization(cdi, idx):
    im = Image.new("RGB", (3840, 2160))
    draw = ImageDraw.Draw(im)
    for k,v in cdi.items():
        for x in idx:
            if(k == 'rect'):
                draw.polygon(list(chain.from_iterable(v)), fill="red")

            elif(k == 'line'):
                draw.line(list(chain.from_iterable(v)), fill="green")

            else:
                draw.polygon(list(chain.from_iterable(v)), fill="yellow")
            im.save(f'Question 1 Images/pillow_imagedraw{x}.jpg', quality=95)
    im.show()


# In[16]:


if __name__ == '__main__':
    print(frequency_of_shapes(label,shape))


# In[18]:


visualization(comb_dict,index)


# In[ ]:




