'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# * Your function should take in a signle parameter 
#  (a string `word`)
# * Your function should return a count of 
#  how many occurences of ***"th"*** occur within `word`. 
#  Case matters.
# * Your function must utilize recursion. 
# * It cannot contain any loops.

# Run `python test_count_th.py` to run the tests for your `count_th()` function to ensure that your implementation is correct.

# Understand - 
# It takes a string, which is indexed like a list
# It looks for occurances of 'th' case sensitive
# It returns an integer of the number of occurances.
# It has to use recursion, not loops

# Plan -
# Base case - return zero if there are no occurances
# Make a variable to return whose default is zero
# Can't use loops but can index into the string and use
# an if statement to add to the variable and add to
# the numbers used to index. this is what I can recurse. 


def count_th(word, sm=0, lg=2, total=0):

    if len(word) == 0:
        return total

    elif lg > len(word):
        return total
    
    else:
        if word[sm:lg] == 'th':
            total += 1
        sm += 1
        lg += 1
        return count_th(word, sm, lg, total)


print(len("abcthxyz"))
print(count_th("abcthxyz"))