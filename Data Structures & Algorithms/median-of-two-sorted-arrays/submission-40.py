from math import inf
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(A) > len(B): A,B = B,A
        total = len(A) + len(B)
        half = total // 2
        l,r = 0,len(A) - 1
        while True:
            i = l + (r-l)//2
            j = half - i - 2
            Al = A[i] if i >= 0 else -inf
            Bl = B[j] if j >= 0 else -inf
            Ar = A[i+1] if i+1<len(A) else inf
            Br = B[j+1] if j+1<len(B) else inf
            if Al <= Br and Bl <= Ar:
                if total % 2: return min(Ar,Br)
                return (min(Ar,Br) + max(Al,Bl)) / 2.
            elif Al > Br: r = i - 1
            else: l = i + 1