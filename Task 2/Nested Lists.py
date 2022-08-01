#!/usr/bin/env python
# coding: utf-8

# In[16]:


final_result=[]
grade_list=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        final_result+=[[name,score]]
        grade_list+=[score]
    l=sorted(list(set(grade_list)))[1] 
    for k,m in sorted(final_result):
        if m==l:
            print(k)


# In[ ]:





# In[ ]:




