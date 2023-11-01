def isPalindrome(s: str) -> bool:
    p1 = 0
    p2 = len(s) - 1
    def skip_nonalpha(s, p1, p2):
        while not s[p1].isalnum():
            p1 += 1
            if p1 >= len(s):
                p1 -= 1
                break
        while not s[p2].isalnum():
            p2 -= 1
            if p2 < 0:
                p1 += 1
                break

        return p1, p2
    p1, p2 = skip_nonalpha(s, p1, p2)
    while p2 > p1:
        if s[p1].lower() != s[p2].lower():
            return False
        p1 += 1
        p2 -= 1
        p1, p2 = skip_nonalpha(s, p1, p2)
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))