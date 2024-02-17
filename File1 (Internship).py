#!/usr/bin/env python
# coding: utf-8

# In[2]:


def func(a, b):
    return b if a == 0 else func(b % a, a)
print(func(30, 75))


# In[3]:


numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))


# In[5]:


set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3 = {99,22,17}

print(len(set1 + set2 + set3))


# In[6]:


import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Get just the current date
current_date = datetime.date.today()
print("Current date:", current_date)

# Create a specific date
specific_date = datetime.date(2024, 2, 13)
print("Specific date:", specific_date)

# Perform computations, e.g., add 1 day to the specific date
one_day_delta = datetime.timedelta(days=1)
next_day = specific_date + one_day_delta
print("Next day:", next_day)


# In[7]:


import datetime

# Create a datetime object
current_datetime = datetime.datetime.now()

# Convert the datetime object to a string with a custom format
formatted_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted string:", formatted_string)


