def swap_case(s):
    res = ''
    for c in s:
        if c.islower():
            res += c.upper()
        elif c.isupper():
            res += c.lower()
        else:
            res += c
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
