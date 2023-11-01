def removeStars(s: str) -> str:
    non_star_indices = []
    s_arr = [c for c in s]
    for i, c in enumerate(s):
        if c != '*':
            non_star_indices.append(i)
        else:
            s_arr[i] = "-"
            s_arr[non_star_indices.pop()] = "-"
    compress = []
    for c in s_arr:
        if c != '-':
            compress.append(c)
    return ''.join(compress)