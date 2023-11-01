def isPalindrome(x: int) -> bool:
        digits = []
        while x >= 10:
            digits.append(x % 10)
            x //= 10
        p1, p2 = 0, len(digits) - 1
        while p1 < p2:
            if digits[p1] != digits[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

print(isPalindrome(10))