class Solution:                
    def largestPerimeter(self, A: List[int]) -> int:
        per = 0
        
        A.sort(reverse=True)
                    
        for i in range (0,len(A)-2):
            if(A[i]<(A[i+1]+A[i+2])):
                sum = A[i]+A[i+1]+A[i+2]
                if(per<sum):
                    per = sum
                    break
                    
        return per
    
    
        
    
            
            
        