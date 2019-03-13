'''

Codewars Kata - 8 Kyu - Tip Calculator

Description:

Write a function, calculateTip(amount, rating) which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive. If an unrecognised rating is input, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
Because you're a nice person, you always round up the tip, regardless of the service.

'''

import math

def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating == 'poor': percentage = 5
    elif rating == 'good': percentage = 10
    elif rating == 'great': percentage = 15
    elif rating == 'excellent': percentage = 20
    elif rating == 'terrible': return(0)

    else:
        return ('Rating not recognised')

    return (math.ceil((float(amount) / 100) * percentage))

