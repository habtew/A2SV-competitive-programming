class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        binary_set = set(int(num, 2) for num in nums)

        for i in range(2**n):
            binary_str = format(i, 'b').zfill(n)
            if int(binary_str, 2) not in binary_set:
                return binary_str