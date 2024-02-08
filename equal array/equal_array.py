class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        A_count = {}
        B_count = {}
        for a in A:
            if a in A_count:
                A_count[a] += 1
            else:
                A_count[a] = 1
        for b in B:
            if b in B_count:
                B_count[b] += 1
            else:
                B_count[b] = 1
        
        return A_count == B_count
