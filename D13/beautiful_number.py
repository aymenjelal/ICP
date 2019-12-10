def main():
    noTest=int(input())
    cases=[]
    lengths=[]
    for i in range(0,noTest):
        length = int(input())
        lengths.append(length)
        case=input()
        cases.append(case.split(" "))

    for j in range(0,len(lengths)):
        print(toCheck(lengths[j],cases[j]))
    

def toCheck(length,case):
    check=""
    for i in range(1,length+1):
        currentNumber=i
        count=0
        for j in range(0,length):
            
            if(int(case[j])>currentNumber):
                count = 0
            else:
                
                count= count+1
            if(count==currentNumber):
                check= check+'1'
                break
            if(j==length-1):
                check= check+'0'
  
    
    return check

if __name__ == "__main__":
    main()