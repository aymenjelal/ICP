def main():
    noTest=int(input())
    cases=[]
    for i in range(0,noTest):
        case=input()
        cases.append(case)

    for j in range(0,noTest):
        currentCase = cases[j]
        lenCase = len(currentCase)
        for i in range(0,lenCase):
            if(i!=lenCase-1):
                if(currentCase[i]==currentCase[i+1] and currentCase[i]!='?'):
                    cases[j]=-1
                    break
            if(currentCase[i]=='?'):
                if(i==0):
                    if(i==lenCase-1):
                        currentCase ='a'
                    else:
                        nextChar= currentCase[i+1]
                        if(nextChar=='a'or nextChar=='b'):
                            currentCase ='c' + currentCase[i+1:]
                        else:
                            currentCase ='a' + currentCase[i+1:]
                elif(i==lenCase-1):
                    previousChar=currentCase[i-1]
                    if(previousChar=='a'or previousChar=='b'):
                        currentCase = currentCase[:i] + 'c'
                    else:
                        currentCase = currentCase[:i] + 'a'
                else:
                    nextChar= currentCase[i+1]
                    previousChar=currentCase[i-1]
                    if((previousChar=='a' and nextChar!='c')or (previousChar=='b' and nextChar!='c')):
                        currentCase = currentCase[:i] + 'c' + currentCase[i+1:]
                    elif((previousChar=='b' and nextChar!='a') or (previousChar=='c' and nextChar!='a')):
                        currentCase = currentCase[:i] + 'a' + currentCase[i+1:]
                    elif((previousChar=='a' and nextChar!='b')or(previousChar=='c' and nextChar!='b')):
                        currentCase = currentCase[:i] + 'b' + currentCase[i+1:]
            cases[j]=currentCase

    for case in cases:
        print(case)



            



if __name__== '__main__':
    main()