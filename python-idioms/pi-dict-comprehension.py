## Idiomatic dict comprehension

# No.1
def i1():
        emails = {user.name: user.email for user in users if user.email}

# No.2
def i2():
        dict_compr = {k: k**2 for k in range(10000)}

# No.3
def i3():
        new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

# No.4
def i4():
        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
        dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}
        print(dict1_tripleCond)

# No.5
def i5():
        nested_dict = {'first':{'a':1}, 'second':{'b':2}}
        float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
        print(float_dict)

# No.6
def i6():    
        # Initialize the `fahrenheit` dictionary 
        fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
        # Get the corresponding `celsius` values and create the new dictionary
        celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
        print(celsius_dict)

# No.7
def i7():
        mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
        mcase_frequency = { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }

