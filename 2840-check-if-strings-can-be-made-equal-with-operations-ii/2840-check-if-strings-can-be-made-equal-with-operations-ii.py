class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # 0, a, c, b == c, b, a
        # 2, b, d, a == a, d, b
        even_s1, odd_s1 = '', ''
        even_s2, odd_s2 = '', ''
        
        for i in range(len(s1)):
            if i % 2 == 0:
                even_s1 += s1[i]
            else:
                odd_s1 += s1[i]
        for i in range(len(s2)):
            if i % 2 == 0:
                even_s2 += s2[i]
            else:
                odd_s2 += s2[i]
              
        even = sorted(even_s1) == sorted(even_s2)
        odd = sorted(odd_s1) == sorted(odd_s2)
        return even and odd