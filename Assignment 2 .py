#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.NO.(1).WAP where user will input the string and program should display all the word starting from alphabet "a" or "A".


# In[2]:


print("enter the string")
s=input()
d=s.split()
for i in d:
    if i.startswith("a") or i.startswith("A") is True:
        print (i)
    else:
        continue;
        


# In[1]:


#Q.NO.(2).WAP where user will enter items for a list and program should remove the duplicate item in the list .


# In[2]:


list1=[]
print("Enter the number of item: ")
s=int(input())
for i in range(1,s+1):
    x=input("enter the items of list: ")
    list1.append(x)
list2=set(list1)
print(list2)


# In[3]:


#Q.NO. (3) Differences between append() & extend() and remove() & pop() method used in list.


# In[11]:


# append() :Add an element to the names list:

names = ['anil', 'niroz', 'ankur']
names.append("arjun")
print(names)


# In[13]:


# extend() :Add the elements of names to the animals list:

animals = ['horse', 'dog', 'donkey']

names= ['anil', 'ankur', 'niroz']

animals.extend(names)
print(animals)


# In[4]:


# remove(): removes the specified item:

list1 = ["anil", "ankur", "niroz","nabin"]
list1.remove("nabin")
print(list1)


# In[9]:


# pop() : removes the specified index, (or the last item if index is not specified):

list1 = ["apple", "banana", "cherry"]
list1.pop()
print(list1)


# In[14]:


# Q.NO.(4).Differences between lists and tuples:


# In[16]:


#LIST :-
#         list is the most used data type in Python. A list can contain the same type of items. Alternatively, a list can also contain different types of items. A list is an ordered and indexable sequence. To declare a list in Python, we need to separate the items using commas and enclose them square brackets([]). The list is somewhat similar to the array in C language. However, an array can contain only the same type of items while a list can contain different types of items. Similar to the string data type, the list also has plus(+), asterik(*) and slicing[:] operators for concatenation, repition and sub-list, respectively. For example;
# 1st list
first = [1,"two",3.0,"four"]
#2nd list
second=["five",6]
#display 1st list 
print(first)


# In[17]:


#concatenate 1st and 2nd  list 
print(first + second)


# In[19]:


#repeat 2nd list 
print(second * 3)


# In[20]:


#display sublist 
print(first[0:2])


# In[23]:


#TUPLE :-
#           Similar to a list, a tuple is also used to store sequence of items. Like a list, a tuple consists of items separated by commas. However, tuples are enclosed within parentheses rather than within square brackets. For example;
third=(7,"eight",9,10.0)
print(third)


# In[24]:


#Q.NO.(5). How can you randomize the item of a list? Explain random module to demonestrate the generation of random number.


# In[ ]:


import random
l=[1,2,3,...]
random.shuffle(l)
print(l)


# In[1]:


x = 1 + 2 * 3 - 4 / 5 ** 6
print (x)


# In[2]:


99/100


# In[14]:


n=10
s=0
t=0
for i in range(1,11):
    if (i%2==0):
        x=-2**(i-1)
        print(x)
        s=s+x
    else:
        y=2**(i-1)
        print(y)
        t=t+y
print(s,t)
print(s+t)


# In[ ]:




