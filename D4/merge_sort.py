def mergeSort(list):
    if(len(list)>1):
        left = list[0:len(list)//2]
        right = list [len(list)//2:]

        mergeSort(left)
        mergeSort(right)

        

        print(left)
        print(right)

        leftPointer = 0
        rightPointer = 0
        orignalPointer = 0

        while leftPointer<len(left) and rightPointer<len(right):
            if(left[leftPointer]>right[rightPointer]):
                list[orignalPointer] = left[leftPointer]
                leftPointer = leftPointer +1
            else:
                list[orignalPointer] = right[rightPointer]
                rightPointer = rightPointer +1
            orignalPointer = orignalPointer +1

        while leftPointer<len(left):
            list[orignalPointer] = left[leftPointer]
            leftPointer = leftPointer +1
            orignalPointer = orignalPointer +1

        while rightPointer<len(right):
            list[orignalPointer] = right[rightPointer]
            rightPointer = rightPointer +1
            orignalPointer = orignalPointer +1
    print(list)




    


if __name__== '__main__':
    list = [4,1,3,2,5]
    mergeSort(list)