## Idiomatic enumerate

# No.1
def i8():
    for i, x in enumerate(l):
        # ...
	
# No.2
def i9():
    try:
        x = next(i for i, n in enumerate(l) if n > 0)
    except StopIteration:
        print('No positive numbers')
    else:
        print('The index of the first positive number is', x)
	
# No.3
def i10():
    ls = list(range(10))
    for index, value in enumerate(ls):
      print(value, index)
  
# No.4
def i11():
    a = [3, 4, 5]
    for i, item in enumerate(a):
        print i, item
	
# No.5
def i12():
    for i, val in enumerate(array):
        #do stuff with i
        #do stuff with val

# No.6
def i13():
    for index, element in enumerate(my_container):
        print (index, element)
	
# No.7
def i14():
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):
        print(c, value)
	
# No.8
def i15():
    my_list = ['apple', 'banana', 'grapes', 'pear']
    counter_list = list(enumerate(my_list, 1))
    print(counter_list)
 
