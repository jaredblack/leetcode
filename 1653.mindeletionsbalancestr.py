# DP topic exam problem 4
# sort of thought of this one from a state machine perspective as well.
# once we exit s0 we cannot go back
def minimumDeletions(s: str) -> int:
    s0 = [1 if s[0] == 'b' else 0]
    s1 = [0]
    for c in s[1:]:
        if c == 'b':
            s0.append(s0[-1] + 1)
            s1.append(min(s0[-1], s1[-1]))
        else:
            s0.append(s0[-1])
            s1.append(min(s0[-1], s1[-1] + 1))
    return min(s0[-1], s1[-1])

print(minimumDeletions("abbababb"))