class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1) 
        n = len(nums2)
        if m > n:
            self.findMedianSortedArrays(nums2,nums1)
        if n == 0:
            raise ValueError
        
        imin,imax,halfLen = 1,m,(m+n+1)/2
        while imin < imax:
            i = (imin + imax)/2
            j = halfLen - i
            if i < m and j > 0 and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and j < n and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = B[j-1]
                if j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1],B[j-1])
            if (m+n)%2 == 1:
                return max_left
            
            if i == m:
                min_right = B[j]
            if j == n:
                min_right = A[i]
            else:
                min_right = min(A[i],B[j])
            
            return float(max_left+min_right)/2
                