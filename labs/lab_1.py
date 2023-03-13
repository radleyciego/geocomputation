# Radley Ciego
# Lab 1

# %%
# Task 1
import random
random.seed(100)
list = []
for i in range(0,10): # length of list
    list.append(random.randint(0,250)) 
print(list)

# %%
def mean(list):
    return sum(list)/len(list)

print(mean(list))
 
 # %%
def variance(list):
    n = len(list)
    mean = sum(list) / n
    deviations = [(x - mean(list)) ** 2 for x in list]
    variance = sum(deviations) / n
    return variance

# %% in
# Cheat Sheet Practice

# For loop - string
for i in "Color":
    print(i)

# For loop - Dictionary
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
for i in car:
    print(car[i]) # logic?

# For tuple loop - Tuple
RYB_color = ("Red", "Yellow", "Blue")
for i in RYB_color:
    print(i)

# The break statement
for i in RYB_color:
    if(i == "Yellow"):
        break
    print(i)

# The continue statement
for i in RYB_color:
    if(i == "Yellow"):
        continue
    print(i) # stops iteration of the loop, continue with next

# the range() function
for i in range(10):
    print(i) # returns a sequence of numbers, starting from 0 by default

for i in range(2,5):
    print(i)

for i in range(2,10,2):
    print(i)

# Else in for loops
for i in range(3):
    print(i)
else:
    print("finally finished")


# %%
