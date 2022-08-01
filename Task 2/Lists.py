#!/usr/bin/env python
# coding: utf-8

# In[18]:


if __name__ == '__main__':
    N = int(input())
    lis=[]
    for i in range(N):
        lis.append(input().split())

    scores=[]
    for i in range(N):
        if lis[i][0]=='insert':
            scores.insert(int(lis[i][1]),int(lis[i][2]))
        elif lis[i][0]=='print':
            print(scores)
        elif lis[i][0]=='remove':
            scores.remove(int(lis[i][1]))
        elif lis[i][0]=='append':
            scores.append(int(lis[i][1]))
        elif lis[i][0]=='pop':
            scores.pop()
        elif lis[i][0]=='sort':
            scores.sort()
        elif lis[i][0]=='reverse':
            scores.reverse()




# In[ ]:





# In[ ]:




