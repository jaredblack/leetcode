import itertools


def mergeAlternately(word1: str, word2: str) -> str:
    res = []
    for i in range(min(len(word1), len(word2))):
        res.append(word1[i])
        res.append(word2[i])
    if len(word1) != len(word2):    
        long_word = word1 if len(word1) > len(word2) else word2
        res.append(long_word[i+1:])
    return ''.join(res)