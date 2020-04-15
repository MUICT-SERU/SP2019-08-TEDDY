# Source: https://www.geeksforgeeks.org/sets-in-python/
# Python program to  
# demonstrate intersection 
# of two sets 
  
set1 = [0,1,2,3,4,5]
set2 = [3,4,5,6,7,8,9]
  
set3 = set1 + set2
unique_set3 = []
for i in set3:
    if i not in unique_set3:
        unique_set3.append(i)
  
print("Intersection using intersection() function") 
print(set3)
print(unique_set3)