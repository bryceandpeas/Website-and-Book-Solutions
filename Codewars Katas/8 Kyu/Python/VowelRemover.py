'''

Codewars Kata - 8 Kyu - Vowel remover

Description:

Create a function called shortcut to remove all the lowercase vowels in a given string.

Examples

shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby
Don't worry about uppercase vowels.

'''

def shortcut( s ):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([l for l in s if l not in vowels])
    