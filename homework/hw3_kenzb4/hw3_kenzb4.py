#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Mackenzie Brown
# Homework 3 
# 9/11/2026


# In[2]:


# dont print problem 1 because there is no code 


# In[1]:


#run imports
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


print("Problem 2") 
#2h
test_square_1 = np.arange(0,10,1) # 0 up to including 9 (no 0., so int)
from hw3_kenzb4_support_module import square #import funt from file (in same dir)
print(square(test_square_1)) #print the function with our made arrays value

#2i
test_square_2 = np.linspace(0., 25., 25).reshape(5,5)
print(square(test_square_2)) #call function to test this array



# In[3]:


print("Problem 3")

from hw3_kenzb4_support_module import squareplot #from file import the function

squareplot(1, 7, 5) # has values 1, 2.5, 4, 5.5, and 7

squareplot(1, 7, 5, "testsquareplot.pdf")


# In[ ]:





# In[ ]:





# In[ ]:




