n = int(input())
phone_book = {}

for _ in range(n):
    key, val = input().split(" ")
    phone_book[key] = val

try:
    while True:
        query = input()
        if not query:
            break
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass
