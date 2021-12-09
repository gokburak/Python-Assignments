#!/usr/bin/env python
# coding: utf-8

# In[ ]:


word = input("kelime giriniz : ")

def not_string(word):
    if word.startswith("not"):
        return(word)
    else:
        return "not " + word
not_string(word)


# In[ ]:




