#!/usr/bin/env python
# coding: utf-8

# # Library for importing a json file

# In[46]:


import json


# In[47]:


def quiz(file):
    with open(file) as json_file:
        data = json.load(json_file) 
    x = list(data.values())
    y=list(x[0].keys())
    print("Select Category")
    print("Press 1 for Sport.")
    print("Press 2 for Maths.")
    user=input()
    answer = []
    if user=='1':
        temp_dict = data['quiz'][y[0]]
        for k,v in temp_dict.items():
            z = dict(v)
            print(z['question'])
            for i in z['options']:
                print(i,"\n")
            answer.append(input("\nEnter the answer:"))
    if user=='2':
        temp_dict = data['quiz'][y[1]]
        for k,v in temp_dict.items():
            z = dict(v)
            print(z['question'])
            for i in z['options']:
                print(i)
            answer.append(input("\nEnter the answer:"))
    return answer


# # Result

# In[48]:


print("choose quiz file")
file=input()
print(quiz(file))


# In[ ]:




