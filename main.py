# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    ### TODO
    set = iterate(parens_update, 1, mylist) #we want to iterate over our entire list, starting with the first element and then complete the iteration
    #until we are left with a single element. if we do not have a single element,then we know the parentheses are NOT balanced
    
    if set == 1:
        return True #if there is only 1 item, then it is by definition balanced
    else:
        return False #there was some parantheses not balanced
    pass


def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    ###TODO
    
    if next_input == '(':
        return current_output + 1 #we designate this as the positive parenthesis for counting purposes
    
    elif next_input == ')':
        if current_output > 1: #we do not want a list of size 0 because that means it is not balanced and we proceed to return False if that is the case
            return current_output - 1 #we designate this as the negative parenthesis for counting purposes 
        else:
            return False
        
    return current_output #we want to return the output after we iterate through our entire list
    
    pass


def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    ###TODO
    list_map = list(map(paren_map, mylist)) #mapping our list to the function paren_map
    scan_map = scan(lambda x,y: x+y, 0, list_map) #we want to scan over our list created from our mapping in the previous line
    scan_reduce = reduce(min_f, 0, scan_map[0]) #we want to call reduce over our mapped scan function in the previous line, calling the conventions 
    #of reduce functions covered in lectures 
    
    if scan_reduce >= 0 and (scan_map[1] == 0): #we want to keep a running tally of what elements of the list we have already scanned and want the 
        #the element located at position 1 to equal 0 because this means our net total of our list is 0, which indicates it is balanced (1-1+0-1+1=0)
        return True
    else:
        return False
    pass

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    ###TODO
    
    #we first need to state our base cases and then build up our recursive solution from there 
    if len(mylist) == 0: #empty list 
        return (0,0)
    
    if len(mylist) == 1: #composed of only ( or ) so we must distinguish what mylist contains
        if mylist[0] == '(':
            return (0,1)
        elif mylist[0] == ')':
            return (1,0)
        else:
            return (0,0) #this means we have an element that is neither ( or ), say an ASCII character 
        
     #recursive step
    #we want to split our list into two halves to implement a divide and conquer approach
    left = parens_match_dc_helper(mylist[(len(mylist)//2):])
    right = parens_match_dc_helper(mylist[:(len(mylist)//2)])
    
    #we compute separate sums because we want to create tuples of our list and recursively go through these tuples until we reach the end of our list
    sum_0 = left[0] + right[0]
    sum_1 = left[1] + right[1]
    
    tuple = (sum_0, sum_1) #tuple with two consecutive sums from consecutive elements in both the left and right sides and we only want to have 2 elements 
    #to compare 
    left_new = tuple[1] - tuple[0]
    right_new = tuple[0] - tuple[1]
    
    if tuple[0] >= tuple[1]: #if the left is greater than the right then we want this sum to be our new left value 
        return (left_new, 0)
    else:
        return (0, right_new)
    pass
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
