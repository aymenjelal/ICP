class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new = []
        notSorted = []
        for i in range(0,len(arr2)):
            count = 0
            for j in range(0,len(arr1)):
                if(arr1[j]==arr2[i]):
                    new.append(arr1[j])
                    count = count + 1
            for k in range (0,count):
                arr1.remove(arr2[i])
                
        for i in range (1,len(arr1)):
            for j in range(i,0,-1):
                if(arr1[j]<arr1[j-1]):
                    temp = arr1[j]
                    arr1[j]= arr1[j-1]
                    arr1[j-1]= temp
        new = new +arr1
                    
        
        return new
        
                    
    
                    
        
        