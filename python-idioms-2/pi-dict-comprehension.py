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
        dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}

# No.5
def i5():
        float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}

# No.6
def i6():    
        celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

# No.7
def i7():
        mcase_frequency = { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }

