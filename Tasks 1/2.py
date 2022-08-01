#!/usr/bin/env python
# coding: utf-8

# In[1]:


if __name__ == '__main__':
    p = int(input().strip())
    if p%2!=0:
        print("Weird")
    elif p>=2 and p<=5:
        print ("Not Weird")
    elif p>=6 and p<=20:
        print ("Weird")
    else:
        print("Not Weird")


# In[ ]:




