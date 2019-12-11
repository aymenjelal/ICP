class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        if(len(s)%2!=0):
            return False
        for i in s:
            if (i=='{' or i =='(' or i=='['):
                opened.append(i)
            elif(i=='}' or i ==')' or i==']'):
                if(len(opened)<1):
                    return False
                last = opened[-1]
                if(i=='}' and last =='{'):
                    opened = opened[0:len(opened)-1]
                elif(i==')' and last =='('):
                    opened = opened[0:len(opened)-1]
                elif(i==']' and last=='['):
                    opened = opened[0:len(opened)-1]
                else:
                    return False
        if(len(opened)==0):
            return True
        else:
            return False
                
                