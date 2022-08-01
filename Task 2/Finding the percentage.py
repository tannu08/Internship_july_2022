#!/usr/bin/env python
# coding: utf-8

# In[17]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    c = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        c += i
    average = c / len(student_marks[query_name])
    print("%.2f" %average)



# In[ ]:





# In[ ]:




