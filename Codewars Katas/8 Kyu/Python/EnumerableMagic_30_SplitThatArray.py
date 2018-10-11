'''

Codewars Kata - 8 Kyu - Enumerable Magic #30 - Split that Array!

Description:

Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.

Here's a simple Ruby example:

animals = ["cat", "dog", "duck", "cow", "donkey"]
partition(animals){|animal| animal.size == 3}
    #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
The equivalent in Python would be:

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
If you need help, here's a reference:

http://www.rubycuts.com/enum-partition

'''

def partition(list, classifier_method):
    new_list = []
    for i in list:
        if classifier_method(i) == True:
            new_list.append(i)
    
    return (new_list, [i for i in list if i not in new_list])