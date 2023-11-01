def isValid(s: str) -> bool:
    open_stack = []
    parens = {')': '(', '}':'{',']':'['}
    for c in s:
        if c in parens.values():
            open_stack.append(c)
        elif len(open_stack) and open_stack[-1] == parens[c]:
            open_stack.pop()
        else:
            return False
    if len(open_stack):
        return False
    return True