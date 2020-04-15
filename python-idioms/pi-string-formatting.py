def i36(Store):
    output = 'ID: {s.branch_ID}, City: {s.city}, Manager: {s.manager}'.format(s=Store)
    return output

def i37():
    class Person:
        def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    person = Person("John", 36, 'M')
    return 'Name: {p.name}\nAge: {p.age}\nGender: {p.gender}'.format(person=p1)

def i38():
    book_info = ' The Three Musketeers: Alexandre Dumas'
    formatted_book_info = book_info.strip().upper().replace(':', ' by').append(', ISBN:')
    
