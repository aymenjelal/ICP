def selection(list):
    for i in range (0,len(list)-1):
        for j in range(0,len(list)-1):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            else:
                break

    return list


if __name__== '__main__':
    list = [39,36,41,47,15,45]
    print(selection(list))