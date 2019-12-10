class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        sorted =[None] * len(A)
        even =0
        odd =1
        for i in range (0,len(A)):
            if(A[i]%2==0):
                sorted[even]=A[i]
                even = even+2
            else:
                sorted[odd]= A[i]
                odd = odd+2
        return sorted
                
        