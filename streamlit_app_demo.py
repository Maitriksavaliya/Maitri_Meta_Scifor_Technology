#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install streamlit')


# In[2]:


# program to check weather the given number is prime or not and if its prime find factorial
import streamlit as st

# check the number is prime/not prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# calculate factorial
def factorial(n):
  if n == 0:
    return 1
  else :
    return n*factorial(n-1)

st.title("factorial of the prime no")

number=st.number_input("enter the number",min_value=0,step=1)

if st.button("check"):
  if is_prime(number):
    st.write(f"{number} is a prime number")
    st.write(f"factorial of {number} is {factorial(number)}")
  else:
    st.write(f"{number} is not a prime number")


# In[3]:




