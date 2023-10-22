#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Create a Python program that asks the user for a month (1-12) and then prints the corresponding season ("Spring," "Summer," "Fall," or "Winter").

def findseason (M) :
     

    list1 = [[12 , 1 , 2], [3 , 4 , 5], 
             [6 , 7 , 8], [9 , 10 , 11]]
              

    if M in list1[0] :
        print ( "WINTER" )
    elif M in list1[1] :
        print ( "SPRING" )
    elif M in list1[2] :
        print ( "SUMMER" )
    elif M in list1[3] :
        print ( "FALL" )
    else :
        print ( "Invalid Month Number" )
 

M = 5
print("For Month number:", M);
findseason ( M )
 
M = 10
print("For Month number:", M);
findseason ( M )


# In[16]:


#Write a Python program that takes two numbers as input and prints the larger number

num1 = int(25)
num2 = int(26)


if num1 > num2:
    print("The larger number is:", num1)
else:
    print("The larger number is:", num2)


# In[1]:


#Create a program that takes an integer as input and checks if it's positive, negative, or zero. Print an appropriate message.


num =float (input("Enter the number:"))
if num > 0:
    print("positive")
elif num == 0:
        print("zero")
else:
    print("negative")


# In[15]:


#Write a Python program that determines whether a given year is a leap year or not. Use the leap year rules mentioned earlier.

year = int(2022)


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# In[19]:


# Write a Python program that asks the user for their age and gender. Based on their age and gender, print a message like "You are a young man" or "You are an old woman."
age = int(22)
gender = ('male')


if age < 40:
    if gender == "male":
        print("You are a young man.")
    else:
        print("You are a young girl.")

elif age >= 40:
    if gender == "male":
        print("You are a old man.")
    else:
        print("You are a old woman.")


# In[24]:


#Create a program that takes a temperature in Celsius and converts it to Fahrenheit. Display the result with an appropriate message.
celsius =float(50)

fahrenheit = (celsius * 9/5) + 32


print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


# In[26]:


#Write a Python program that calculates the shipping cost based on the weight of a package. Use the following rules:
#Weight <= 2 pounds: $5.00
#2 pounds < Weight <= 10 pounds: $10.00
#Weight > 10 pounds: $15.00

weight = float(50)


if weight <= 2:
    shipping_cost = 5.00
elif weight <= 10:
    shipping_cost = 10.00
else:
    shipping_cost = 15.00

print(f"The shipping cost for a {weight} pound package is ${shipping_cost:.2f}")


# In[28]:


#Create a program that asks the user for three numbers and then prints them in ascending order.

num1 = float(20)
num2 = float(35)
num3 = float(60)

numbers = [num1, num2, num3]


numbers.sort()


print("Numbers in ascending order:", numbers)


# In[2]:


#Write a Python program that checks if a given year is a "century year" (ends in 00). If it's a century year, check if it's a leap year.

year = int(2022)

if:
is_century = year % 100 == 0

else:
    is_leap_year = year % 4 == 0

    if is_leap_year:
        print("is a century year.")
    else:
        print("is a leap year.")


# In[1]:


#Create a program that asks the user for a number and then determines if it's even or odd. Print an appropriate message.

number = int(5)


if number % 2 == 0:
    print("is an even number.")
else:
    print("is an odd number.")


# In[ ]:




