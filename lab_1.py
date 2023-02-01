# Radley Ciego
# Lab 1

# Task 1
import random
random.seed(100)
list = []
for i in range(0,10): # length of list
    list.append(random.randint(0,250)) 
print(list)

def mean(list):
    return sum(list)/len(list)
print(mean(list))