from collections import Counter
def isSubset( a1, a2, n, m):
    count_a1 = Counter(a1)
    count_a2 = Counter(a2)
    answer = "Yes"
    for key, val in count_a2.items():
        if val > count_a1[key]:
            answer = "No"
            break
    return answer
