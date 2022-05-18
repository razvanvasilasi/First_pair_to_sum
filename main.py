def sum_pairs(lst, s):
    seen = set()
    for num in lst:
        if num in seen:
            return [s-num, num]
        seen.add(s-num)
