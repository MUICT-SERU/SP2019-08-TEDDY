# Source: https://www.geeksforgeeks.org/sets-in-python/
# Python program to  
# demonstrate intersection 
# of two sets 
  
set1 = {0,1,2,3,4,5}
set2 = {3,4,5,6,7,8,9}
  
# Intersection using 
# intersection() function 
set3 = set(set1.union(set2)) 
  
print("Intersection using intersection() function") 
print(set3)