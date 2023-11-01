# efficiency boost: split the string on '(' then split again in ')' when it becomes important
def evaluate(s: str, knowledge: list[list[str]]) -> str:
    know_dict = {pair[0]:pair[1] for pair in knowledge}
    final = s
    i = 0
    while i < len(s):
        if s[i] == '(':
            start = i
            end = i
            for j in range(i, len(s)):
                if s[j] == ')':
                    end = j
                    break  
            key = s[i+1:end]
            if key in know_dict:
                final = final.replace(s[start:end+1], know_dict[key])
            else:
                final = final.replace(s[start:end+1], '?')
            i = end
        i += 1
    return final

print(evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))