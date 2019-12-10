def quickSort(list,start,end):
    if(start<end):
        partitionIndex = partition(list,start,end)
        quickSort(list,start,partitionIndex-1)
        quickSort(list,partitionIndex+1,end)
    


def partition(list,start,end):
    pivot= list[end]
    partitionIndex=start
    for i in range(start,end-1):
        if(list[i]<= pivot):
            list[i],list[partitionIndex] = list[partitionIndex],list[i]
            partitionIndex=partitionIndex+1
    list[partitionIndex],list[end] = list[end],list[partitionIndex]
    return partitionIndex


if __name__== '__main__':
    list = [4,3,5,2]
    quickSort(list,0,len(list)-1)
    print (list)