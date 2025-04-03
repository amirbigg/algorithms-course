def merge_the_tools(string, k):
    uniques = []
    for i in range(0, len(string), k): # 0 3 6
        u = ""
        for ch in string[i:i+k]:
            if ch not in u:
                u = u + ch
        uniques.append(u)
    print("\n".join(uniques))


merge_the_tools('AAABCADDE', 3)