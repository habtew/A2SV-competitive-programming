class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1, left2 = 0, 0
        right1, right2 = len(nums1) - 1, len(nums2) - 1

        result = []
        while left1 <= right1 and left2 <= right2:
            if nums1[left1] < nums2[left2]:
                result.append(nums1[left1])
                left1 += 1
            else:
                result.append(nums2[left2])
                left2 += 1
        result.extend(nums1[left1:])
        result.extend(nums2[left2:])
        i = len(result) // 2
        if len(result) % 2 == 0:
            return (result[i] + result[i - 1]) / 2

        return result[i]