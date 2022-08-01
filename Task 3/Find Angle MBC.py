#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
xyz=int(input())
bc=int(input())
abc=math.hypot(xyz,bc)
klm=abc/2
bca=math.asin(1*xyz/abc)
bm=math.sqrt((bc**2+klm**2)-(2*bc*klm*math.cos(bca)))
mbc=math.asin(math.sin(bca)*klm/bm)
print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')



# In[ ]:





# In[ ]:




