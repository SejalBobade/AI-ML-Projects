#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to perform basic operations on two numbers
def basic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else 'undefined'  
    return addition, subtraction, multiplication, division



# In[2]:


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
results = basic_operations(num1, num2)
print("Addition:", results[0])
print("Subtraction:", results[1])
print("Multiplication:", results[2])
print("Division:", results[3])




# In[3]:


import random

# Create a list of 10 random integers
random_list = [random.randint(1, 100) for _ in range(10)]
print("Original List:", random_list)

# Sort the list in ascending and descending order
ascending = sorted(random_list)
descending = sorted(random_list, reverse=True)

# Find the minimum and maximum values in the list
minimum = min(random_list)
maximum = max(random_list)

# Calculate the average of the list
average = sum(random_list) / len(random_list)

print("Sorted (Ascending):", ascending)
print("Sorted (Descending):", descending)
print("Minimum Value:", minimum)
print("Maximum Value:", maximum)
print("Average:", average)





# In[4]:


# Create a dictionary of student names and their marks
students = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'David': 88,
    'Eva': 95
}

# Display all student names
print("Student Names:", list(students.keys()))

# Display all marks
print("Marks:", list(students.values()))

# Find the student with the highest marks
highest_student = max(students, key=students.get)
print("Student with Highest Marks:", highest_student, "with marks", students[highest_student])



# In[5]:


# Program to manipulate a sentence
sentence = input("Enter a sentence: ")

# Convert to uppercase
upper_sentence = sentence.upper()

# Count vowels
vowels = "AEIOU"
vowel_count = sum(1 for char in sentence if char.upper() in vowels)

# Reverse the sentence
reversed_sentence = sentence[::-1]

print("Uppercase:", upper_sentence)
print("Number of Vowels:", vowel_count)
print("Reversed Sentence:", reversed_sentence)



# In[6]:


import numpy as np


# In[7]:


# Create a 1D NumPy array with numbers from 1 to 10
array = np.arange(1, 11)

# Reshape the array into a 2x5 matrix
reshaped_array = array.reshape(2, 5)

# Find the mean, median, and standard deviation
mean_value = np.mean(array)
median_value = np.median(array)
std_deviation = np.std(array)

# Select elements at even indices
even_index_elements = array[::2]

print("Reshaped Array:", reshaped_array)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
print("Elements at Even Indices:", even_index_elements)


# In[8]:


import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 32, 25],
    'Salary': [50000, 62000, 48000]
}
df = pd.DataFrame(data)

# Display the first two rows
print(df.head(2))

# Add a new column "Department"
df['Department'] = ['HR', 'IT', 'Finance']

# Remove the "Age" column
df = df.drop(columns=['Age'])

print("Updated DataFrame:", df)


# In[9]:


# Create a DataFrame for employee data
data = {
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
    'Employee': ['John', 'Anna', 'Peter', 'Mike', 'Linda'],
    'Salary': [50000, 62000, 48000, 52000, 58000]
}
df = pd.DataFrame(data)

# Group the data by the "Department" column
grouped_df = df.groupby('Department')['Salary'].mean().reset_index()

print("Average Salary by Department:", grouped_df)



# In[10]:


# Creating a DataFrame with dates
date_data = {
    'Dates': ['2024-01-01', '2024-02-15', '2024-03-20']
}
df = pd.DataFrame(date_data)
df['Dates'] = pd.to_datetime(df['Dates'])

# Extract year, month, day
df['Year'] = df['Dates'].dt.year
df['Month'] = df['Dates'].dt.month
df['Day'] = df['Dates'].dt.day

# Calculate the difference between two dates
date_diff = (df['Dates'][1] - df['Dates'][0]).days

print("Extracted Year, Month, Day:", df)
print("Difference between two dates:", date_diff, "days")


# In[11]:


# Create a DataFrame with some missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 5, 6, 7],
    'C': [8, 9, 10, None]
}
df = pd.DataFrame(data)

# Identify missing values
print("Missing Values:", df.isnull())

# Fill missing values with the mean of the respective column
df_filled = df.fillna(df.mean())

# Drop any rows that still contain missing values
df_dropped = df_filled.dropna()


# In[ ]:





# In[ ]:




