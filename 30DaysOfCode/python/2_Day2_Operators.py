'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/tutorials/30-days-of-code

Hackerrank - 30 Days Of Code - Day 2: Operators

Objective 
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are 33 lines of numeric input: 
The first line has a double, mealCostmealCost (the cost of the meal before tax and tip). 
The second line has an integer, tipPercenttipPercent (the percentage of mealCostmealCost being added as tip). 
The third line has an integer, taxPercenttaxPercent (the percentage of mealCostmealCost being added as tax).

Output Format

Print 𝚃𝚑𝚎 𝚝𝚘𝚝𝚊𝚕 𝚖𝚎𝚊𝚕 𝚌𝚘𝚜𝚝 𝚒𝚜 𝚝𝚘𝚝𝚊𝚕𝙲𝚘𝚜𝚝 𝚍𝚘𝚕𝚕𝚊𝚛𝚜.The total meal cost is totalCost dollars., where totalCosttotalCost is the rounded integer result of the entire bill (mealCostmealCost with added tax and tip).

contact: bryce@brycefury.com

'''

meal_cost = float(input())
tip_percentage = float(input())
tax_percentage = float(input())

tip_amount = (meal_cost * (tip_percentage/100))
tax_amount = (meal_cost * (tax_percentage/100))

total_cost = meal_cost + tip_amount + tax_amount

print ("The total meal cost is " + str(round(total_cost)) + " dollars.")
