def main():
    num1 = input ("Enter first number ")
    num2 = input ("Enter second number ")

    num1Neg = False
    num2Neg = False

    length1 = len(num1)
    length2 = len(num2)

    if(num1[0]=='-'):
        num1Neg = True
        num1 = num1[1:length1+1]
        length1 = length1 -1 
    
    if(num2[0]=='-'):
        num2Neg = True
        num2 = num2[1:length2+1]
        length2 = length2-1


    if(length1<=length2):
        maxlength = length2
        minlength = length1
        minNum = num1
        maxNum = num2
    else:
        maxlength = length1
        minlength = length2
        minNum = num2
        maxNum = num1
    
    multiples = []
    carry =0

    for i in range (minlength-1,-1,-1):
        row = ""
        for j in range (maxlength-1,-1,-1):
            temp = (int(maxNum[j])* int(minNum[i])+carry)%10
            carry =(int(maxNum[j])* int(minNum[i])+carry)//10
            

            row = str(temp)+row
            if(j == 0 and carry!=0):
                
                row = str(carry)+row
        carry =0

        for k in range (i,minlength-1,1):
            row = row+"0"
        
                
        multiples.append(row)

    print(str(multiples))

    mulSum = "0"
    for i in range (0,len(multiples)):

        num = multiples[i]

        length1 = len(num)
        length2 = len(mulSum)

        if(length1>=length2):
            maxlength = length1
            if(length1!=length2):
                for i in range(maxlength-length2):
                    mulSum = '0'+mulSum
        else:
            maxlength = length2
            for i in range(maxlength-length1):
                num = '0'+num

        carry = 0
        sum=""

        for digits in range (maxlength-1,-1,-1):
            temp1 = int(num[digits])
            temp2 = int(mulSum[digits])

            temp = (temp1+temp2+carry)%10
            carry = (temp1+temp2+carry)//10

            sum= str(temp)+sum
            if(digits == 0 and carry!=0):
                sum = str(carry)+sum

        mulSum = sum

    if(num1Neg and not num2Neg):
        mulSum="-"+mulSum
    
    elif (num2Neg):
        mulSum= "-"+mulSum

    print(mulSum)
        












main()