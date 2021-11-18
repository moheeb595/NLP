#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1)Sentence tokenizing
text="""
Are you fascinated by the amount of text data available on the internet? Are you looking for ways to work with this text data but aren’t sure where to begin? Machines, after all, recognize numbers, not the letters of our language. And that can be a tricky landscape to navigate in machine learning.
"""


# In[2]:


from nltk.tokenize import sent_tokenize


# In[3]:


t1=''
t1=sent_tokenize(text)


# In[4]:


for s in t1:
    print(s)


# ## 
# 2)word splitting

# In[5]:


for i in range(len(text)):
    i=text.split()
    
print(i)


# ### 
# 3)stemming

# In[6]:


from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize


# In[7]:


w1=["cats","trouble","troubling","troubled","having","Corriendo","at","was"]
a1=PorterStemmer()


# In[8]:


for i in w1:
    print(a1.stem(i))


# In[9]:


#Lemmatization
from nltk.stem import WordNetLemmatizer
l1=WordNetLemmatizer()


# In[10]:


for j in w1:
    print(l1.lemmatize(j))


# In[11]:


#4) Finding stop words
text1="""
“The NLTK library is one of the oldest and most commonly used Python libraries for Natural Language Processing. NLTK supports stop word removal, and you can find the list of stop words in the corpus module. To remove stop words from a sentence, you can divide your text into words and then remove the word if it exits in the list of stop words provided by NLTK.”
"""


# In[12]:


from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
words=word_tokenize(text1)
l1=[]
for w in words:
    if w not in stop_words:
        l1.append(w)


# In[13]:


print(l1)


# In[14]:


#5)printing frequency of each word
from nltk.probability import FreqDist
t1=[t for t in text1.split()]
f1=FreqDist(t1)
l1=[(k,v) for k, v in f1.items()]
print(l1)


# In[ ]:




