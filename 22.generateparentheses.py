def generateParenthesis(n: int) -> list[str]:
    all_poss = []
    def gen(parens, num_to_close, pairs_started):
        if len(parens) == n * 2:
            all_poss.append(parens)
            return
        if num_to_close > 0:
            gen(parens + ')', num_to_close - 1, pairs_started)
        if pairs_started < n:
            gen(parens + '(', num_to_close + 1, pairs_started + 1)
    
    gen('(', 1, 1)
    return all_poss

