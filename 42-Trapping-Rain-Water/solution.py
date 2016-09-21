class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,water,leftmax,rightmax = 0,len(height)-1,0,0,0
        while i<= j:
            leftmax = max(leftmax,height[i])
            rightmax= max(rightmax,height[j])
            if height[i] < height[j]:
                water += (leftmax-height[i])
                i += 1
            else:
                water += (rightmax - height[j])
                j -= 1
        return water