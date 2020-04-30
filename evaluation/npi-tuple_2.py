# Exerpted from https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/
# Program to understand about  
# packing and unpacking in Python 
  
# this lines PACKS values 
# into variable a 
a = ("MNNIT Allahabad", 5000, "Engineering")   
  
# this lines UNPACKS values 
# of variable a 
college = a[0]
student = a[1]
type_ofcollege = a[2]
  
# print college name 
print(college) 
  
# print no of student 
print(student) 
  
# print type of college 
print(type_ofcollege) 