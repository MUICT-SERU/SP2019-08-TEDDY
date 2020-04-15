## Non-idiomatic dict comprehension

# No.1
def n1():
    emails = {}
    for user in users:
      if user.email:
        emails[user.name] = user.email

# No.2
def n2():
    d = {}
    for k in range(10000):
        d[k] = k**2
	
# No.3
def n3():
    for n in numbers:
        if n%2==0:
            new_dict_for[n] = n**2

# No.4
def n4():
    dict1_tripleCond = {}
    for (k,v) in dict1.items():
        if (v>=2 and v%2 == 0 and v%3 == 0):
                dict1_tripleCond[k] = v
    print(dict1_tripleCond)

# No.5
def n5():
    nested_dict = {'first':{'a':1}, 'second':{'b':2}}
    for (outer_k, outer_v) in nested_dict.items():
        for (inner_k, inner_v) in outer_v.items():
            outer_v.update({inner_k: float(inner_v)})
    nested_dict.update({outer_k:outer_v})
    print(nested_dict)

# No.6
def n6():
    fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
    #Get the corresponding `celsius` values
    celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
    #Create the `celsius` dictionary
    celsius_dict = dict(zip(fahrenheit.keys(), celsius))
    print(celsius_dict)

