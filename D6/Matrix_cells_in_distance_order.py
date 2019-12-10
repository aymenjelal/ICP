class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dis=[]
        cor=[]
        for i in range (0,C):
            for j in range(0,R):
                x = abs(j-r0)
                y = abs(i-c0)
                
                dis.append(x+y)
                cor.append([j,i])
                
        dis, cor = zip(*sorted(zip(dis, cor)))
                
        
            
        return cor
            
                
        