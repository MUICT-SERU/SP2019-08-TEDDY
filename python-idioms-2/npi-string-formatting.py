def n38(Store):
    return 'ID: ' + Store.branch_ID + ' City: ' + Store.city + ' Manager: ' + Store.manager

def n39(Store):
    return 'ID: %i City: %s Manager: %s' % (Store.branch_ID, Store.city, Store.Manager)

def n40(self, name, age, gender):
    return 'Name: ' + person.name + '\nAge: ' + person.age + '\nGender: ' + person.gender

def n41(self, name, age, gender):
    return 'Name: %s\nAge: %i\nGender: %c' % (person.name, person.age, person.gender) 

def n42():
    formatted_book_info = book_info.strip()
    formatted_book_info = formatted_book_info.upper()
    formatted_book_info = formatted_book_info.replace(':', ' by')

def n43(setence):
    output = sentence.capitalize()
    output = output.swapcase()
    output = output.replace('I\'m', 'I am')
    output = output.replace('You\'re','You are')
    output = output.replace('can\'t','cannot')
    
def n44(setence):
    formatted = sentence.capitalize()
    formatted = formatted.swapcase()

