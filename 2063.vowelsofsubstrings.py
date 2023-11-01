
# this seems to be one of those ones where you just need to
# figure out the formula. I sort of get it but I'm not sure
# if I would've come up with it on my own
def countVowels(word: str) -> int:
    V = {'a','e','i','o','u'}
    l = len(word)
    ct = 0
    for i, c in enumerate(word):
        if c in V:
            ct += (l - i) * (i + 1)
    return ct

print(countVowels("aabbb"))