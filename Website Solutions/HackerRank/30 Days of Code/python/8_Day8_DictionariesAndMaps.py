'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/tutorials/30-days-of-code

Hackerrank - 30 Days Of Code - Day 8: Dictionaries and Maps

Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for; for each  queried, print the associated entry from your phone book (in the form ) or  if there is no entry for .

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format

The first line contains an integer, , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line. The first value is a friend's , and the second value is an -digit .

After the  lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English letters and are first names only.

Constraints

Output Format

On a new line for each query, print  if the name has no corresponding entry in the phone book; otherwise, print the full  and  in the format .

Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933
Explanation


We add the  subsequent (Key,Value) pairs to our map so it looks like this:


We then process each query and print  if the queried Key is found in the map, or otherwise.

Query 0:
Sam is one of the keys in our dictionary, so we print .

Query 1:
Edward is not one of the keys in our dictionary, so we print .

Query 2:
Harry is one of the keys in our dictionary, so we print .

contact: bryce@brycefury.com

'''

N = int(input())
dic = {}

for i in range(0,N):
    name, number = input().split()
    dic[name] = number



for j in range(0,N):
    name = input()
    if name in dic:
        print (name + '=' + dic[name])
    else:
        print ('Not found')

