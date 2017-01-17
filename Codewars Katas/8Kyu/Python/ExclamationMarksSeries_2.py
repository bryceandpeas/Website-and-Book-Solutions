'''

Codewars Kata - 8 Kyu - Exclamation marks series #2: Remove all exclamation marks from the end of sentence

Description:

Remove all exclamation marks from the end of sentence.
Examples

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"
Note

Please don't post issue about difficulty or duplicate.

'''

def remove(s):
    return(s.rstrip('!'))