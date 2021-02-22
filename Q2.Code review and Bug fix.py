#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import csv
from PIL import Image


# In[2]:


color_key = [(1, 1, 1), (0, 0, 0)]
rejected_img = []


# In[3]:


def iterate_folder(directory, directory_in_str):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        taskid = filename.split('_')[1]
        if filename.endswith('.png'):
            check_colors(directory_in_str, filename)


# In[4]:


def check_colors(directory_in_str, filename):
    corrected_path = os.path.join(directory_in_str, filename)
    img = Image.open(corrected_path)
    colors = img.getcolors()
    if colors:
        for color in colors:
            if color[1] not in color_key:
                if filename not in rejected_img:
                    rejected_img.append(filename)


# In[5]:


def create_csv(directory_in_str, rejected_img):
    with open(directory_in_str + '_reporting.csv', 'w') as outputcsv:
        csv_output = csv.writer(outputcsv)
        csv_output.writerow(['filename'])
        for img in rejected_img:
            csv_output.writerow(img)


# In[6]:


from Question_2 import iterate_folder,check_colors,create_csv

rejected_imgs = ['indexed_5d5da9038aa716043cb777f4_0e2ee618-dab5-48c1-b13f-13ca3f8326e6.png', 'indexed_5d5da90b8aa716043cb77aee_1ab53596-6e32-45b6-a1e0-061678e7bd23.png', 'indexed_5d5da90c8aa716043cb77b51_ca9f07f5-5f7b-4143-9b94-ed8691b6e5fe.png', 'indexed_5d5ef9676fa52f01d898a8ae_7cd19bd9-17de-489a-b56d-2062244a1ab3.png', 'indexed_5d5ef9756fa52f01d898ac71_b083d50f-090d-4597-a9dd-001915b174dd.png', 'indexed_5d8161b98a68b4007cacac32_3a9a7392-effd-461f-95d4-44a61fd8d35d.png', 'indexed_5d8161b98a68b4007cacac34_1400c1d9-e129-4c2d-9420-f45faad725b7.png', 'indexed_5d8161b98a68b4007cacac35_bdb8c04e-0220-45be-8117-caa3879f81ed.png', 'indexed_5d8161b98a68b4007cacac36_9975c866-79a8-4166-8647-fe1e7f376122.png', 'indexed_5d8161b98a68b4007cacac37_0dcf9e36-8a8a-485d-b70e-2238d9ab8a5e.png', 'indexed_5d8161b98a68b4007cacac38_87575520-718a-452a-974c-e11ef15ddca3.png', 'indexed_5d8161b98a68b4007cacac39_8a526e18-cba6-4778-b4ef-475d2ba90665.png', 'indexed_5d8162010568a7003591aee6_b24bac0c-4c7e-4c6d-9d1c-1cb509d80f51.png', 'indexed_5d8162010568a7003591aee7_ed11a398-dc5d-4ee5-bb07-ce426f59cc73.png', 'indexed_5d8162010568a7003591aee8_29733c09-b4da-4c1c-88a3-23bad02f8e48.png', 'indexed_5d8162010568a7003591aee9_3cbc332a-0f57-4557-9433-8a232932dd3e.png', 'indexed_5d8162010568a7003591aeea_a6a24a31-6809-4414-aa8d-73318e292e1f.png', 'indexed_5d8162010568a7003591aeeb_30652a19-6c6e-4d9c-b80c-03dc31643048.png', 'indexed_5d8162010568a7003591aeec_a398c705-620e-4812-a21e-4131bd8f24ce.png', 'indexed_5d8162010568a7003591aeec_a398c705-620e-4812-a21e-4131bd8f24cg.png', 'indexed_5d8162010568a7003591aeec_a398c705-620e-4812-a21e-4131bd8f24dr.png', 'indexed_5d8162010568a7003591aeec_a398c705-620e-4812-a21e-4131bd8f25ac.png', 'indexed_5d8162010568a7003591aeed_e8a10ee3-f911-444f-9f2f-11565ad162ca.png', 'indexed_5d8162010568a7003591aeee_94ed4379-ae5a-41e3-883e-cb78dd37683b.png', 'indexed_5d8162010568a7003591aeef_390ff273-b031-4864-8cdf-a6389eeec1e6.png', 'indexed_5d8162010568a7003591aef0_2c7aa0a2-7a53-421d-ae28-e3ad6b13ec24.png', 'indexed_5d8162010568a7003591aefa_59ab3fe6-07d4-45e3-8341-6ab52ccfd716.png', 'indexed_5d8162010568a7003591aefb_132a196c-1157-4a35-87d0-f1950f9ce78a.png', 'indexed_5d8162010568a7003591aefc_e0e6bf4b-ad58-480f-80e1-c197f9bf7155.png', 'indexed_5d8162010568a7003591aefd_bd377c70-7724-427a-9da9-1ba81e15b857.png', 'indexed_5d8162010568a7003591aefe_82db2556-080e-4e65-8567-253ee3c2c7c3.png', 'indexed_5d8162010568a7003591aeff_610356f3-fd46-4527-82b7-47319d928d5b.png', 'indexed_5d8162010568a7003591af00_fcc568dd-3f08-4beb-a51a-1f1ab774f65a.png', 'indexed_5d8162010568a7003591af01_263d1ef7-736f-46f3-8518-3cf1a7e69335.png', 'indexed_5d8162010568a7003591af02_eee50fb2-99b4-452d-a45e-12c68d32682e.png', 'indexed_5d8162108a68b40085acac2b_8abf8d9e-f5e0-457f-a506-2afd5d2c5bfa.png', 'indexed_5d8162108a68b40085acac2c_032850fe-a149-49c5-9499-d275c424bdfe.png', 'indexed_5d8162108a68b40085acac2d_b0304d63-f980-4cf0-8027-60a1eb055a77.png', 'indexed_5d8162108a68b40085acac2e_bb48fb49-5126-41ed-b77a-9e24a281c331.png', 'indexed_5d8162108a68b40085acac2f_1385c70e-ac33-4283-aed6-cd51e33af96c.png']
fname = 'indexed_5d5da9038aa716043cb777f4_0e2ee618-dab5-48c1-b13f-13ca3f8326e6.png'
directory_in_str = r"C:\\Users\\Mehul\\Desktop\\cse-technical-exercise-master\\Question_1_Example_Images\\Question 2 Images"
directory = b'C:\\Users\\Mehul\\Desktop\\cse-technical-exercise-master\\Question_1_Example_Images\\Question 2 Images'

def test_iterate_folder():
    assert iterate_folder(directory, directory_in_str) == None 

def test_check_colors():
    assert check_colors(directory_in_str, fname ) == None

def test_create_csv():
    assert create_csv(directory_in_str, rejected_imgs) == None


# ##From the above the as you can see i tried to create a list of the rejected images then i put the file in two directories, one where i can iterate the images within a folder and second to create a string to save the color details in a csv file so that it is more readable although i did not get the desired results.
