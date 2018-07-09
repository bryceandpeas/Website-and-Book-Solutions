'''

Codewars Kata - 8 Kyu - Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence

Description:

Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
Note
Please don't post issue about difficulty or duplicate. Because:

That's unfair on the kata creator. This is a valid kata and introduces new people to javascript some regex or loops, depending on how they tackle this problem. --matt c



'''

def replace_exclamation(s):
    return "".join(map(lambda x: '!' if x in "aeiouAEIOU" else x, s))