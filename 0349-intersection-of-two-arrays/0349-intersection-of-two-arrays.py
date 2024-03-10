class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_list = []
        i = 0
        j = 0

        nums2 = sorted(set(nums2))
        while (i < len(nums2)):
            if nums2[i] in nums1:
                new_list.append(nums2[i])
            i += 1
        return new_list