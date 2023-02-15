def isValid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    "(())][{}"
    """
    stack = []
    pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
            }
    for item in s:
        if item in pairs:
            stack.append(item)
        elif not stack or item != pairs[stack.pop()]:
            return False
    return len(stack) == 0

        
        
    
