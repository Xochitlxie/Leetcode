class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,max,leftmax,rightmax = 0,len(height)-1,0,0,0
        while i<= j:
            leftmax = max(leftmax,height[i])
            rightmax= max(rightmax,height[j])
            if height[i] < height[j]:
                max += (leftmax-height[i])
                i += 1
            else:
                max += (rightmax - height[j])
                j -= 1
        return max