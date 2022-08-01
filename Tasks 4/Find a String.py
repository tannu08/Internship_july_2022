#!/usr/bin/env python
# coding: utf-8

# In[6]:


def count_substring(string, sub_string):
    countt = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            countt += 1
    return countt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:





# In[ ]:




