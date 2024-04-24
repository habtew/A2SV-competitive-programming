class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_great = {}
    
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_great[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            if num in next_great:
                res.append(next_great[num])
            else:
                res.append(-1)
        return res