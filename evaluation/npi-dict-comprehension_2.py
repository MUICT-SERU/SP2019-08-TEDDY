# Source: https://www.geeksforgeeks.org/python-dictionary-comprehension/
# Python code to demonstrate dictionary  
# comprehension 
  
# Lists to represent keys and values 
keys = ['a','b','c','d','e'] 
values = [1,2,3,4,5]   
  
# but this line shows dict comprehension here   
myDict = {}
for k:v in zip(keys,values):
    myDict[k] = v

# We can use below too 
# myDict = dict(zip(keys, values))   
  
print (myDict)