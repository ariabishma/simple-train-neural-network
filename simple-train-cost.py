
# coding: utf-8

# In[172]:


def cost(b):
    return (b-4) ** 2


# In[185]:


def num_slope(b):
    h = 0.0001
    return (cost(b+h) - cost(b))/h


# In[165]:


def slope(b):
    return  2 * (b-4)


# In[217]:


b = 3
for i in range(10):
    b = b - .1 * slope(b)
    print(b)


# In[216]:


cost(b)

