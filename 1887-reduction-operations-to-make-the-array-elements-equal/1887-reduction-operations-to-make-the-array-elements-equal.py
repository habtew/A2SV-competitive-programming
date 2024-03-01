class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        element_indices = defaultdict(list)
        unique_sorted_elements = sorted(set(nums))

        if len(unique_sorted_elements) == 1:
            return 0

        for index, element in enumerate(nums):
            element_indices[element].append(index)

        total_operations = 0
        for index, unique_element in enumerate(unique_sorted_elements):
            total_operations += index * len(element_indices[unique_element])

        return total_operations