# DP topic exam problem 2
def minimumTotal(triangle: list[list[int]]) -> int:
    inverted_result = [triangle[-1]]
    for row in reversed(triangle[:-1]):
        result_row = []
        for i, n in enumerate(row):
            result_row.append(min(inverted_result[-1][i], inverted_result[-1][i+1]) + n)
        inverted_result.append(result_row)
    return inverted_result[-1][-1]


print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))