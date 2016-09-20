'''

Codewars Kata - 8 Kyu - Count of positives / sum of negatives

Description:

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array:

C#/Java: new int[] {} / new int[0];
C++: std::vector<int>();
JavaScript/CoffeeScript/PHP: [];

'''

def count_positives_sum_negatives(arr):
    positive_count = 0
    negative_sum = 0
    output = []
    
    for i in arr:
        if i > 0:
            positive_count += 1
        else:
            negative_sum += int(i)
            
    output.append(positive_count)
    output.append(negative_sum)
    
    return (output)