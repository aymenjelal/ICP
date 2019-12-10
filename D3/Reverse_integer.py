class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if(x<0):
            if(x<(-2)**31):
                return 0
            isNeg = True
            
            x = x*-1
        elif(x>0):
            if(x>(2**31)-1):
                return 0
            
        reverse = 0
        prevRev = 0
        while (x!=0):
            rem = x%10
            x = x//10
            reverse = (reverse*10) +rem
            if (reverse >= 2147483647 or reverse <= -2147483648): 
                reverse = 0
            if((reverse-rem)//10!=prevRev):
                return 0
            prevRev = reverse;
        if(isNeg):
            reverse = -1*reverse
        return reverse
            
        