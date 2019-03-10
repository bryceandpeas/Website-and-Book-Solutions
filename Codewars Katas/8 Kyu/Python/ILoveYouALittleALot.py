'''

Codewars Kata - 8 Kyu - I love you, a little , a lot, passionately ... not at all

Description:

Who remembers the time where in the schoolyard, girls take flower petals. Tears saying:

I love you
a little
a lot
passionately
madly
not at all
When the last petal torn comes to the word 'madness', these are cries of excitement, dreams and emotions surging in thoughts.

Your goal in this kata is to define the result of such a game given nb_petals > 0, the number of petals torn.

'''

def how_much_i_love_you(nb_petals):
    out_list = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    return(out_list[(nb_petals % len(out_list)) - 1])
