class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends_list = list(range(1, n + 1))

        current_index = 0
        while len(friends_list) > 1:
            current_index = (current_index + k - 1) % len(friends_list)
            friends_list.pop(current_index)
        return friends_list[-1]