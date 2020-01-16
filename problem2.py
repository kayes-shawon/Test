# Program to find the depth of dictionary as well as able to handle Python object

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
        
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
    
def print_depth(data, level=1):
    """
    Function to print all the keys of the dictionary and object 
    with their depth
    """
    for key, value in data.items():
        if isinstance(value, dict):
            print("{0} : {1}".format(key, level))
            print_depth(value, level+1)
        elif isinstance(value, Person):
            print("{0} : {1}".format(key, level))
            obj_dict = value.__dict__
            print_depth(obj_dict, level+1)
        else:
            print("{0} : {1}".format(key, level))
        
print_depth({'key1':1, 'key2': { 'key3': 1, 'key4': {'key5':4, 'user': person_b}}})

