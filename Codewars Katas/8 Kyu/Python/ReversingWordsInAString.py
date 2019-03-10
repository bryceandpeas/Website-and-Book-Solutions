'''

Codewars Kata - 8 Kyu - Reversing Words in a String

Description:

Caution: This kata does not currently have any known supported versions for Python. It may not be completable due to dependencies on out-dated libraries/language versions.
You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

reverse('Hello World') == 'World Hello'
reverse('Hi There.') == 'There. Hi'
Happy coding!


'''

def reverse(st):
    return ' '.join((st.split(' ')[::-1]))