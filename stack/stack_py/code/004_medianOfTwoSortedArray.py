class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m 
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            i = (imin+imax)//2
            j = half_len - i
            if i<m  and nums2[j-1]>nums1[i]:
                imin = i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax = i-1
            else:
                if i==0: maxLeft = nums2[j-1]
                elif j==0: maxLeft = nums1[i-1]
                else: maxLeft = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1:
                    return maxLeft
                
                if i==m: minRight = nums2[j]
                elif j==n: minRight = nums1[i]
                else: minRight = min(nums1[i], nums2[j])

                return (maxLeft+minRight)/2.0