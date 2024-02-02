class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uniq_nums1 = []
        uniq_nums2 = []
        combined = [*nums1, *nums2]
        
        for num in combined:
            if num in nums1 and num not in nums2:
                if num in uniq_nums1:
                    continue
                uniq_nums1.append(num)
            elif num in nums2 and num not in nums1:
                if num in uniq_nums2:
                    continue
                uniq_nums2.append(num)
        return [uniq_nums1, uniq_nums2]