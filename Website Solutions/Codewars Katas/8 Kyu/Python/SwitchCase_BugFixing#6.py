"""

Codewars Kata - 8 Kyu - Switch/Case - Bug Fixing #6

Description:

Switch/Case - Bug Fixing #6

Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object, can you fix timmy's function?

"""

def eval_object(v):
    return {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'], }[v['operation']]





