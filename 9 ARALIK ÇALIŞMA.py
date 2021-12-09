#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# word = input("kelime giriniz : ")

# def not_string(word):
#     if word.startswith("not"):
#         return(word)
#     else:
#         return "not " + word
# not_string(word)


# In[ ]:



sentence = input('Enter a Sentence :')
result = {}

for i in sentence :
    if i not in result :
        result[i] = 1
    else :
        result[i] += 1
print(result)


# In[ ]:




