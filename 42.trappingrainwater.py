def trap(height: list[int]) -> int:
    max_left = 0
    max_right = len(height) - 1
    water = 0
    for i, n in enumerate(height):
        if i == 0: continue
        if n > height[max_right]:
            max_right = i
    for i, n in enumerate(height):
        if i == 0: continue
        water += max(0, min(height[max_left], height[max_right]) - n)
        if i == max_right:
            old_max_right = max_right
            max_right = i + 1
            for j in range(old_max_right + 1, len(height)):
                if height[j] > height[max_right]:
                    max_right = j
        if n > height[max_left]:
            max_left = i
    return water


print(trap([5,4,1,2]))