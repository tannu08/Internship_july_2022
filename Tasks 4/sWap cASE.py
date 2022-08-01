#!/usr/bin/env python
# coding: utf-8

# In[2]:


def swap_case(s):
    score = []
    for letter in s:
        if letter == letter.lower():
            score.append(letter.upper())
        elif letter == letter.upper():
            score.append(letter.lower())
        else:
            score.append(letter) 
    return ''.join(score)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:





# In[ ]:




