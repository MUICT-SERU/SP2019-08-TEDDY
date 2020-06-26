## Non-idiomatic enumerate

# No.1
def n7():
    for i in range(len(l)):
        x = l[i]
    try:
        x = next(i for i, n in enumerate(l) if n > 0)
    except StopIteration:
        print('No positive numbers')
    else:
        print('The index of the first positive number is', x)
	
# No.2
def n8():
    x = next(n for n in l if n > 0)
	
# No.3
def n9():
    ls = list(range(10))
    index = 0
    while index < len(ls):
      print(ls[index], index)
      index += 1
  
# No.4
def n10():
    # Add three to all list members.
    a = [3, 4, 5]
    b = a  #a and b refer to the same list object
    for i in range(len(a)):
        a[i] += 3 #b[i] also changes
	
# No.5
def n11():
    for i in range(len(array)):
        #do stuff with i
        #do stuff with array[i]
	
# No.6
def n12():
    index = 0
    for element in my_container:
        print (index, element)
        index+=1

