if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner, runner_up = float('-inf'), float('-inf')
    for num in arr:
        if num > winner:
            runner_up = winner
            winner = num
        elif num > runner_up and num != winner:
            runner_up = num
    print(runner_up)
