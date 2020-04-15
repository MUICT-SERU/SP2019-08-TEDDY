# Source: https://www.programiz.com/python-programming/file-operation
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()