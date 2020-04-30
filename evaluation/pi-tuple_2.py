# Source: https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/
# Program to understand about  
# packing and unpacking in Python 
  
# this lines PACKS values 
# into variable a 
a = ("MNNIT Allahabad", 5000, "Engineering")   
  
# this lines UNPACKS values 
# of variable a 
(college, student, type_ofcollege) = a   
  
# print college name 
print(college) 
  
# print no of student 
print(student) 
  
# print type of college 
print(type_ofcollege) 
