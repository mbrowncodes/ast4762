#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Mackenzie Brown
# Practicum 1 
# 9/11/2026


# In[ ]:





# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits


# In[48]:


# Problem 1 (no AI)

# make array 300x200 with loop
x = np.zeros((300,200))
print(x.shape) # size and shape of array
print(x.dtype) # shows float array type 
for i in range(300):
    x[i,:] = i # for all values of 

print(x[100])
plt.imshow( x, cmap='gray', origin = 'lower') # flip so 0,0 bottom left, gray colormap
plt.show()



# In[46]:


# array without loop (worked out in class together)
y = np.arange(300.) # create a look with x values 0-299, no y
y.shape=(300,1) #add y value
#check print statement for .shape and .dtype (300,200) and float
arr = np.zeros((300,200)) #fill in with float 0.0

arr+=y # add the values of same shape arrays 


plt.imshow( arr, cmap='gray', origin = 'lower') 
plt.show()


# In[31]:


# Problem 2 (with AI)

print("Google Gemini Chatbox: Copy and Pasted Prompt")

A = Float[(j-1) for i in 1:300, j in 1:200]

A = ones(Float64,300) * (0:199)

A = zeros(Float64, 300) .+ (0:199)'

# first prompt ran alone provided code in another language


# In[39]:


# 2nd chat prompt ran

# with a loop
A_loop = np.zeros((200,300), dtype=np.float64)
for col in range(300):
    for row in range(200):
        A_loop[row, col] = col

# without a loop
A = np.tile(np.arange(300, dtype=np.float64), (200,1))

plt.imshow(A, cmap='gray')
plt.colorbar(label='y coordinate')
plt.title('300x200 Array Visualized')
plt.xlabel("Column (y coordinate)")
plt.ylabel("Row")
plt.show()


# In[40]:


# 3rd chat prompt ran
A = np.tile(np.arange(300, dtype=np.float64), (200,1))

plt.imshow(A, cmap='gray', origin='lower')
plt.colorbar(label ='y coordinate')
plt.title('300x200 Array (Origin:Lower-Left)')
plt.xlabel("Column (y coordinate)")
plt.ylabel("Row")
plt.show()


# In[53]:


print("Google Gemini Chatbox: Edited Prompts")

# without a loop
y_coords = np.arange(300, dtype=np.float64)

array_no_loop = np.tile(y_coords, (200, 1)).T

print("Shape:", array_no_loop.shape) 
print("Dtype:", array_no_loop.dtype)  
print("First row:", array_no_loop[0, :5])  
print("First column sample:", array_no_loop[:5, 0])

y = np.arange(300, dtype=np.float64)
x = np.arange(200, dtype=np.float64)
_, array_no_loop = np.meshgrid(x, y)

array_with_loop = np.empty((300, 200), dtype=np.float64)

# with a loop
for i in range(300):
    array_with_loop[i, :] = float(i)

print("Shape:", array_with_loop.shape)  
print("Dtype:", array_with_loop.dtype)  


# In[54]:


import matplotlib.pyplot as plt
import numpy as np

# 1. Create the 300x200 float64 array
array = np.tile(np.arange(300, dtype=np.float64), (200, 1)).T

# 2. Check random array elements (row index = y coordinate)
np.random.seed(42)  # For reproducible random coordinates
random_rows = np.random.randint(0, 300, size=5)
random_cols = np.random.randint(0, 200, size=5)

print("--- Random Element Checks ---")
for r, c in zip(random_rows, random_cols):
    print(f"Array element at [y={r}, x={c}]: {array[r, c]}")

# 3. Plot the array
plt.figure(figsize=(6, 8))
img = plt.imshow(
    array,
    cmap="gray",
    origin="lower",  # Sets [0, 0] to the bottom-left corner
    aspect="auto",  # Keeps image dimensions responsive
)

plt.colorbar(img, label="Y Coordinate Value")
plt.xlabel("X Index (0 to 199)")
plt.ylabel("Y Index (0 to 299)")
plt.title("300x200 Array (Bottom-Left = 0,0)")

plt.tight_layout()
plt.show()


# In[3]:


# Problem 3

file_path = '/Users/mackenziebrown/Documents/ast4762/lecture_notes/week_3/m42_40min_ir.zip'
# in another directory, define path to .zip file
fits.open(file_path) #open the file

hdr = fits.getheader(file_path)
#print(hdr)      #find info like CTYPE1&2 for X&Y axis details

fits.info(file_path) # tells type, dimension, about file
im = fits.getdata(file_path) # data as im variable so we can plot

plt.imshow(im, cmap = 'gray', origin = 'lower') # origin lower left, gray plot
plt.title("Messier 42: Orion Nebula, Mackenzie") # object name + my name
plt.xlabel("Right Ascension (R.A.)")
plt.ylabel("Declination (DEC)")
plt.savefig('practicum1_kenzb4_problem3_plot1.png')

#fits.info('file_path')


# In[ ]:




