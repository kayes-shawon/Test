# Python3 Program to find depth of a dictionary
def print_depth(data, level=1):
    for key, value in data.items():
        if isinstance(value, dict):
            print("{0} : {1}".format(key, level))
            print_depth(value, level+1)
        else:
            print("{0} : {1}".format(key, level))
        
print_depth({'key1':1, 'key2': { 'key3': 1, 'key4': {'key5':4}}, 'key6': 9})
