class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for i in nums:
            count[i] = count[i]+1
        
        counter = 0
        for j in range(0,3):
            while(count[j]!=0):
                nums[counter]= j
                counter = counter +1
                count[j] = count[j]-1
                
                