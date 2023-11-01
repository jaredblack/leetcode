def climbStairs(n: int) -> int:
    m1, m2 = 1, 2
    if n == 1:
        return m1
    if n == 2:
        return m2   
    for _ in range(2, n):
        m3 = m1 + m2
        m1 = m2
        m2 = m3
    return m3    
