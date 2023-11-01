def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    sets = []
    for i, _ in enumerate(s1):
        for set in sets:
            if s1[i] in set or s2[i] in set:
                set.update({s1[i], s2[i]})
                break
        else:
            sets.append({s1[i], s2[i]})
    consolidated_sets = []
    for set in sets:
        megaset = set
        for other_set in sets:
            if not set.isdisjoint(other_set):
                megaset.update(other_set)
        consolidated_sets.append(megaset)
    sets = consolidated_sets

    final_str = []
    for s in baseStr:
        for set in sets:
            if s in set:
                final_str.append(min(set))
                break
        else:
            final_str.append(s)
    return ''.join(final_str)

print(smallestEquivalentString("cgokcgerolkgksgbhgmaaealacnsshofjinidiigbjerdnkolc", "rjjlkbmnprkslilqmbnlasardrossiogrcboomrbcmgmglsrsj", "bxbwjlbdazfejdsaacsjgrlxqhiddwaeguxhqoupicyzfeupcn"))