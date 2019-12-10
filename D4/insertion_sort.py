def insertion(list):
    for i in range (1,len(list)):
        for j in range(i,0,-1):
            if(list[j]<list[j-1]):
                temp = list[j]
                list[j]= list[j-1]
                list[j-1]= temp
    return list
if __name__== '__main__':
    list = [39,36,41,47,15,45]
    print(insertion(list))
