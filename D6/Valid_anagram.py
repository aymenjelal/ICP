class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        for i in t:
            count = 0
            for j in s:
                if(i==j):
                    if(count<len(s)-1):
                        s = s[0:count]+s[count+1:]
                    elif(count==0):
                        s = s[count+1:]
                    else:
                        s = s[0:count]
                    break
                    
                count = count+1
                
        if(len(s)>0):
            return False
        else:
            return True
        