class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greator = {}
    
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greator[stack.pop()] = num
            stack.append(num)
        
        for rem in stack:
            next_greator[rem] = -1
        result = [next_greator.get(num, -1) for num in nums1]
        return result