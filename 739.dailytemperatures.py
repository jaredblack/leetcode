def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    res = [0 for _ in range(len(temperatures))]
    for i, temp in enumerate(temperatures):
        if len(stack) == 0:
            stack.append((temp, i))
        else:
            while len(stack) and temp > stack[-1][0]:
                index = stack.pop()[1]
                res[index] = i - index
            stack.append((temp, i))
    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))