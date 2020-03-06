## Idiomatic list comprehension

# No.1
def i21():
        result_list = [el for el in range(10000000)]

# No.2
def i22():
        [print(i) for i in wordList]
        

def i23():
        new_list = [n**2 for n in numbers if n%2==0]

def i24():
        ls = [element for element in range(10) if not(element % 2)]

def i25():
        valedictorian = max([(student.gpa, student.name) for student in graduates])

def i26():
        a = [3, 4, 5]
        b = a
        a = [i + 3 for i in a]

def i27():
        return [[float(a_ij) for a_ij in a_i] 
            for a_i in matrix_of_anything]