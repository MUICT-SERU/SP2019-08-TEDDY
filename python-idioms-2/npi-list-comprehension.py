## Non-idiomatic list comprehension

# No.1
def n18():
    result_list = []
    for el in range(10000000) :
        result_list.append(el)
	
# No.2
def n19():
    for i in range(len(wordList)) :
        print(wordList[i]) 
        i += 1

# No.3
def n20():
    ls = []
    for element in range(10):

# No.4
def n21():
    new_list = []
    for n in numbers:
		
# No.5
def n22():
    list = [1, 3, 5, 7, 9] 
    while i < length: 
	
# No.6
def n23():
    ls = list(filter(lambda element: not(element % 2), range(10)))

# No.7
def n24():             
    for i in range(len(a)):
        a[i] += 3 
	
# No.8
def n25(matrix_of_anything):
    new_matrix_of_floats = []
    for i in xrange(0, n):
        row = []
        for j in xrange(0, n_i):
            row.append(float(matrix_of_anything[i][j]))
        new_matrix_of_floats.append(row)
    
