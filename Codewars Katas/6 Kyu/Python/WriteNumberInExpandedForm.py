'''

Codewars Kata - 6 Kyu - Write Number In Expanded Form

Description:

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

'''

def expanded_form(num):
    num_len = len(str(num))
    out_string = ''
    for i in str(num):
        if i != '0':
            out_string += (''.join(i + ('0' * (num_len - 1))))
            num_len -= 1
            if num_len > 0 and num_len < len(str(num)):
                out_string += ' + '
        else:
            num_len -= 1
            continue

    return(out_string.strip(' + '))
