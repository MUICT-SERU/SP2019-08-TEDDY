## Non-idiomatic file reading statement

# No.1
def n13():
    f = open('file.txt')
    a = f.read()
    f.close()

# No.2
def n14():
    f = open(path, "rb")
    result = do_something_with(f)
    f.close()

# No.3
def n15():
    f = open('file.ext')
    try:
      contents = f.read()
    finally:
      f.close()
  
# No.4
def n16():
    file = open("welcome.txt")
    file.close() 

# No.5
def n17():
    file_handle = open(path_to_file, 'r')
