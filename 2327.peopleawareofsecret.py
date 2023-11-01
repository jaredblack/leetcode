def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    # BOUNDS CHECK
    spread = [0 for _ in range(n)]
    spread[0] = 1
    total = 0
    for i in range(n):
        total += spread[i]
        if spread[i] > 0:
            for j in range(i + delay, i + forget):
                if j >= n:
                    break
                spread[j] += spread[i]
            if i + forget < n:
                total -= spread[i]

    return total


print(peopleAwareOfSecret(425,81,118))