'''

Codewars Kata - 8 Kyu - Welcome to the City

Description:

Create a method say_hello that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space betweeen each, and the length of the name array in test cases will vary.

Example

say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

'''

def say_hello(name, city, state):
    return('Hello, '+ ' '.join(i for i in name) + '! Welcome to ' + city + ', ' + state + '!')