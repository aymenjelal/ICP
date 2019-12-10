class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter =[]
        for i in nums1:
            for j in nums2:
                if (i==j):
                    if(j in inter):
                        break
                    inter.append(j)
                    nums2.remove(j)
                    break
        return inter
        