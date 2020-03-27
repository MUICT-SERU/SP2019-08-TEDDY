## Idiomatic file reading statement

# No.1
def i16():
    with open('file.txt') as f:
        for line in f:
            print line
		
# No.2
def i17():
    with open(path, "rb") as f:
        result = do_something_with(f)
        print("Got result: {}".format(result))

# No.3
def i18():
    with open('file.ext') as f:
        contents = f.read()
  
# No.4
def i19():
    with open("welcome.txt") as file: 
        data = file.read()
        do something with data

# No.5
def i20():
    with open(path_to_file, 'r') as file_handle:
        for line in file_handle:
            if raise_exception(line):
                print('No! An Exception!')
 
