'''

Codewars Kata - 8 Kyu - String Templates - Bug Fixing #5

Description:

Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template feature, Help Timmy with his string template so it works as he expects!

'''

def build_string(*args):
    return "I like {0}!".format(", ".join(args))
