def prefix(list):
    operands = []
    while(len(list)>=1):
        current = list.pop()
        if(current=='+' or current=='-' or current=='*' or current=='/'):
            operand1=operands.pop()
            operand2=operands.pop()
            if(current=='+'):
                operands.append(operand1+operand2)
            elif(current=='-'):
                operands.append(operand2-operand1)
            elif(current=='*'):
                operands.append(operand2*operand1)
            elif(current=='/'):
                operands.append(int(float(operand2)/float(operand1)))
                    
        else:
            operands.append(int(current))

    return operands

if __name__== '__main__':
    list = ["*","+","1","3","-","2","3"]
    print(prefix(list))

