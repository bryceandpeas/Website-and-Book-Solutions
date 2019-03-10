"""

Monday 25th April 2016

Hackerrank - Python - Sets - The Captain's Room

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of KK members per group where KK ≠ 11.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear KK times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of KK and the room number list.

Input Format

The first line consists of an integer, KK, the size of each group.
The second line contains the unordered elements of the room number list.


Constraints

1<K<10001<K<1000
Output Format

Output the Captain's room number.



"""

#times out all testcases except #0 and #9, unsure why

K = input()
rooms = list(input())

print (''.join([x for x in rooms if rooms.count(x) == 1]))






