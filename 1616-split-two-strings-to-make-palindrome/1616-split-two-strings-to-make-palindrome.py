class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a, b):
            i, j = 0, len(b) - 1
            while i < j and a[i] == b[j]:
                i, j = i + 1, j - 1
          
            return i >= j or is_palindrome_substring(a, i, j) or is_palindrome_substring(b, i, j)
      
        def is_palindrome_substring(s, start, end):
            return s[start:end+1] == s[start:end+1][::-1]
      

        return check(a, b) or check(b, a)
