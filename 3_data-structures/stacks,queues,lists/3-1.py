'''
[3] A common problem for compilers and text editors is determining whether the parentheses in a string are balanced and properly nested.
For example, the string ((())())() contains properly nested pairs of parenthesees, while the strings )()( and ()) do not.
Give an algorithm that returns true if a string contains properly nested and balanced parentheses, and false if otherwise.
For full credit, identify the position of the first offending parenthesis if the string is not properly nested and balanced. 
'''

'''
- iterate through given string:
    - for '(': insert into stack with index in string.
    - for ')': pop from stack.
        - if stack is empty, means not enough '(' ==> return index of offending ')'
- if at the end, the stack is not empty, return the first index of the item(s) in the stack.
'''

def validateParentheses(s):
    stack = []

    for idx, char in enumerate(s):
        if char == '(':
            stack.append(idx)
        else:
            if not stack: # too many ')'
                return False, idx
            else:
                stack.pop()
    
    if stack:
        return False, stack[0]
    else:
        return True, None



# test cases:
s = "((())())()"
print(validateParentheses(s))

s = ")()("
print(validateParentheses(s))
            
s = "()("
print(validateParentheses(s))