## Idiomatic enumerate

# No.1
def i8():
    for i, x in enumerate(l):
	
# No.2
def i9():
    try:
        x = next(i for i, n in enumerate(l) if n > 0)
    except StopIteration:
        ##
    else:
	
# No.3
def i10():
    for index, value in enumerate(ls):
  
# No.4
def i11():
    for i, item in enumerate(a):
	
# No.5
def i12():
    for i, val in enumerate(array):

# No.6
def i13():
    for index, element in enumerate(my_container):
	
# No.7
def i14():
    for c, value in enumerate(my_list, 1):
	
# No.8
def i15():
    counter_list = list(enumerate(my_list, 1))
 
