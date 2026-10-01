#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sabrina Ratliff
#Practicum 3
#9/25/26















# In[21]:


import numpy as np
import matplotlib.pyplot as plt
import linfit
import scipy.special as ss


# In[7]:


data = np.loadtxt('practicum3_1.dat') #calls in data from dat file


# In[8]:


# from 'practicum3_1.dat', Model 1 only goes from line 1 to line 102
# so to graph Model 1, we only want this data


# In[14]:


x_model1 = [row[0] for row in data[:100]]  #pulls x column from data set only for Model 1

y_model1 = [row[1] for row in data[:100]]  #pulls f(x) column from data set only for Model 1


# In[26]:


plt.scatter(x_model1, y_model1, color='blue', alpha=0.7, label='Model 1 (Data + Noise)')
plt.title('Model 1: f(x)=3.2x + 1.2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()


# In[22]:


#1a use linfit


# In[32]:


y1 = np.array(y_model1)
x1 = np.array(x_model1)


# In[35]:


fit_1 = linfit.linfit(y1, x1, 0.5)  #linefit to the data with a standard deviation of 0.5


# In[36]:


#Parameters
print("The intercept of the fit is:", fit_1[0])
print("The slope of the fit is:", fit_1[1])
print("Uncertainty of the intercept:", fit_1[2])
print("Uncertainty of the slope:", fit_1[3])
print("Chi-squared:",fit_1[4])
print("Probability of finding worse Chi-squared for this model:",fit_1[5])
print("Covariance matrix:",fit_1[6])
print("Model array:", fit_1[7])


# In[39]:


print('Question 1b')
print('Changing the standard deviation value changes the Chi-squared value') 
print('A standard deviation of 0.2 would produce a larger chi-squared value, while a standard deviation of 0.9 would produce a smaller chi-squared.')
print('Either way skews the fitline. Deciding on a standard deviation value is important to getting the right fit.')


# In[96]:


z_s = np.abs(fit_1[1] - 3.2) / fit_1[3] #z-value gives how many standard deviations the fit is away from the data
z_i = np.abs(fit_1[0] - 1.2) / fit_1[2]

print('The slope is within',z_s,'standard deviations')
print('The y-intercept is within',z_i,'standard deviations')


# In[97]:


print('Yes the data is within 3 standard deviations')


# In[43]:


print('Question 1c')
print('The probability of getting a worse chi-squared value is', fit_1[5])


# In[49]:


plt.scatter(x_model1, y_model1, color='blue', alpha=0.7, label='Model 1 (Data + Noise)')
plt.plot(x_model1, fit_1[7], color = 'red', label= 'Model 1 fit') 
plt.title('Model 1: f(x)=3.2x + 1.2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig('P3_sabrinaly_question1c_graph1.png')
plt.show()


# In[55]:


#Question 1d, repeat process for Model 2
x_model2 = [row[0] for row in data[100:203]]  #pulls x column from data set only for Model 2

y_model2 = [row[1] for row in data[100:203]]  #pulls f(x) column from data set only for Model 2


# In[56]:


#Plot of Model 2
plt.scatter(x_model2, y_model2, color='blue', alpha=0.7, label='Model 2 (Data + Noise)')
plt.title('Model 2: f(x)=3.2x^2 + 1.2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()


# In[57]:


y2 = np.array(y_model2)
x2 = np.array(x_model2)


# In[58]:


fit_2 = linfit.linfit(y2, x2, 0.5)  #linefit to the data with a standard deviation of 0.5


# In[59]:


#Parameters
print("The intercept of the fit is:", fit_2[0])
print("The slope of the fit is:", fit_2[1])
print("Uncertainty of the intercept:", fit_2[2])
print("Uncertainty of the slope:", fit_2[3])
print("Chi-squared:",fit_2[4])
print("Probability of finding worse Chi-squared for this model:",fit_2[5])
print("Covariance matrix:",fit_2[6])
print("Model array:", fit_2[7])


# In[60]:


plt.scatter(x_model2, y_model2, color='blue', alpha=0.7, label='Model 2 (Data + Noise)')
plt.plot(x_model2, fit_2[7], color = 'red', label= 'Model 2 fit') 
plt.title('Model 1: f(x)=3.2x^2 + 1.2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig('P3_sabrinaly_question1d_graph2.png')
plt.show()


# In[61]:


print('Question 1d')
print('No the linear fit does not fit the data')
print('The fit line is designed to fit a linear data set, while Model 2 is a quadratic data set')
print('The chi-squared value is also very large. We want a small chi-squared value to accept the fit of the data')
print('Probablity of a worse chi-squared value is 0; we ideally want a value greater than 0.1')


# In[ ]:





# In[101]:


#Question 2
print('Question 2')


# In[63]:


poisson = np.random.poisson(lam=10000, size=396) #poisson part of array. First 396 values of array
uniform = np.random.uniform(low=0, high=10e6, size=4) #uniform part of array. Last 4 values


# In[64]:


final_array = np.concatenate([poisson, uniform]) #combines into one 400 element array


# In[66]:


print('The mean of the dataset is:', np.mean(final_array))
print('The median of the dataset is:', np.median(final_array))


# In[99]:


# N= 10000
print('The median is much closer to N than the mean')


# In[103]:


print('Question 2b')


# In[102]:


med = np.median(final_array) #median of final array
std = np.std(final_array)  #standard deviation of data
upp_limit = med + (5 * std)
low_limit = med - (5 * std)
subsample = final_array[(final_array >= low_limit) & (final_array <= upp_limit)] #where final array is 5sigma away from median


# In[94]:


# mean, median, and std of subsample
s_mean = np.mean(subsample)
s_med = np.median(subsample)
s_std = np.std(subsample)
print('The mean of the subsample is:', s_mean)
print('The median of the subsample is:', s_med)
print('The standard deviation of the subsample is:', s_std)


# In[100]:


print('The mean and standard deviation has significantly decreased since outliers are no longer included in the set')
print('The median has stayed about the same')
print('This is because the subsample was created around how close the data values were to the median')


# In[ ]:




