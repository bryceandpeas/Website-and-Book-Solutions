'''

Hackerank Domains: https://www.hackerrank.com/domains

Python https://www.hackerrank.com/domains/python

Date and Time: https://www.hackerrank.com/domains/python/py-date-time

Hackerrank - Python - Date and Time - Time Delta

Timestamps are given in the format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. See the sample below for details.

Task
Given  timestamps, print the absolute difference (in seconds) between them.

Input Format
The first line contains , the number of testcases.
Each testcase contains  lines, representing time  and time .

Output Format
Print the absolute difference  in seconds.

Constraints
It is guaranteed that the input contains only valid timestamps, and the year can reach up to .

Sample Input

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 +0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 +0000
Sample Output

25200
88200

'''


import calendar
import time

T = int(input())

for i in range(T):
    collect_times = []

    for j in range(2):
        all_times = (input().rsplit(' ', 1))

        check_zone = all_times[1][:1]
        get_time = calendar.timegm(time.strptime(all_times[0], "%a %d %b %Y %H:%M:%S"))
        time_zone = calendar.timegm(time.strptime('1970' + all_times[1][1:], "%Y%H%M"))

        if check_zone == '+': adjusted_time = get_time  - time_zone
        if check_zone == '-': adjusted_time = get_time  + time_zone
        collect_times.append(adjusted_time)

    print(abs(collect_times[0] - collect_times[1]))





