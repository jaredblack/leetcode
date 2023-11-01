# slow because of string concatenation but whatever

def gcdOfStrings(str1: str, str2: str) -> str:
    running_divisor = ''
    divisor = ''
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            running_divisor += str1[i]
        if str1.count(running_divisor) * len(running_divisor) == len(str1) and \
           str2.count(running_divisor) * len(running_divisor) == len(str2):
            divisor = running_divisor
        
    return divisor
