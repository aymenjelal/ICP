def counting(list):
    dic={}
    sort=[]
    max = 0
    min = 0
    for i in list:
        if(i>max):
            max = i
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1

    for i in range(0,max+1):
        if i in dic:
            while(dic[i]!=0):
                print(i)
                sort.append(i)
                dic[i] = dic[i]-1

    return sort



if __name__== '__main__':
    list = [3,2,4]
    print(counting(list))