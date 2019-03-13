'''

Codewars Kata - 8 Kyu - Grasshopper - Terminal Game Turn Function

Description:

Terminal game turn function

You are creating a text-based terminal version of your favorite board game. In the board game, each turn has six steps that must happen in this order: roll the dice, move, combat, get coins, buy more health, and print status.

You are using a library that already has the functions below. Create a function named doTurn/do_turn that calls the functions in the proper order as described in the paragraph above.

- `combat`
- `buy_health`
- `get_coins`
- `print_status`
- `roll_dice`
- `move`

'''

def do_turn():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()