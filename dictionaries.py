'''Dictionaries examples'''

# Create dictionary with dict()
spanish = dict()

spanish['ciao'] = 'hola'
spanish['si'] = 'si'
spanish['uno'] = 'uno'
spanish['due'] = 'dos'

print(spanish['due'])

# Another way of using dict():
dictionary2 = dict(one=1, two=2)
print(dictionary2['one'])

# Another way of using dict() and zip:
# The zip() function returns a zip object, which is an iterator of tuples where
# the first item in each passed iterator is paired together, and then the second item in each passed iterator are
# paired together etc.
dictionary3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(dictionary3['two'])

# Another way of using dict():
dictionary4 = dict({'one' : 1, 'two': 2})
print(dictionary4['one'])

# Another way of defining dictionaries, with curly brackets {}:
spanish3 = {'tre': 'tres', 'quattro': 'cuatro'}

print(spanish3['quattro'])


# Use of function to create dictionaries
def createDictionary():
    spanish = dict()
    spanish['ciao'] = 'hola'
    spanish['si'] = 'si'
    spanish['uno'] = 'uno'
    spanish['due'] = 'dos'
    return spanish


def main():
    dictionary = createDictionary()
    print(dictionary['ciao'])


main()
