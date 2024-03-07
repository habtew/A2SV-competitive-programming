class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        
        while right < len(chars):
            if chars[right] != chars[left]:
                diff = right - left
                if diff > 1:
                    arr = list(str(diff))
                    chars[left + 1:right] = arr
                    right = left + len(arr) + 1
                left = right
            else:
                right += 1

        diff = right - left
        if diff > 1:
            arr = list(str(diff))
            chars[left + 1:] = arr
            return left + len(arr) + 1
        else:
            return len(chars)