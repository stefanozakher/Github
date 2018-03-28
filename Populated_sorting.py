
# coding: utf-8

# In[ ]:


def populated_sorting(num_list):
    sorted_list=[]
    for i in range(0,len(num_list)):
        small=num_list[0]
        for i in range(0,len(num_list)):  
            if small>num_list[i]:
                small=num_list[i]
        sorted_list.append(small)
        num_list.remove(small)
    return sorted_list
populated_sorting([54,26,93,17,77,31,44,55,20])

