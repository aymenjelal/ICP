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
    
     
     
    if(length1>=length2):
        maxlength = length1
        if(length1!=length2):
            for i in range(maxlength-length2):
                num2 = '0'+num2
    else:
        maxlength = length2
        for i in range(maxlength-length1):
            num1 = '0'+num1

    carry = 0
    sum = ""

    if(num1Neg and num2Neg):

        for digits in range (maxlength-1,-1,-1):
            temp1 = int(num1[digits])
            temp2 = int(num2[digits])

            temp = (temp1+temp2+carry)%10
            carry = (temp1+temp2+carry)//10
            sum= str(temp)+sum
        sum = '-'+sum

    elif(num1Neg):
        for digits in range (maxlength-1,-1,-1):
            temp1 = int(num1[digits])
            temp2 = int(num2[digits])-carry

            if(temp2<temp1):
                if(digits != 0):
                    carry = 1
                    temp2 = temp2 +10
                    temp = temp2 - temp1
                    sum= str(temp)+sum
                else:
                    temp = temp2 - temp1
                    
                    sum= str(temp)+sum
            else:
                temp = temp2 - temp1
               
                if(digits==0 and temp!=0):
                    sum= str(temp)+sum
                elif(digits!=0):
                    sum= str(temp)+sum
                
                
                carry = 0

    elif(num2Neg):

        for digits in range (maxlength-1,-1,-1):
            temp1 = int(num1[digits])-carry
            temp2 = int(num2[digits])

            if(temp1<temp2):
                if(digits != 0):
                    carry = 1
                    temp1 = temp1 +10
                    temp = temp1 - temp2
                    sum= str(temp)+sum
                else:
                    temp = temp1 - temp2
                    
                    sum= str(temp)+sum
            else:
                temp = temp1 - temp2
               
                if(digits==0 and temp!=0):
                    sum= str(temp)+sum
                elif(digits!=0):
                    sum= str(temp)+sum
                
                
                carry = 0
            

    
    else:
        for digits in range (maxlength-1,-1,-1):
            temp1 = int(num1[digits])
            temp2 = int(num2[digits])

            temp = (temp1+temp2+carry)%10
            carry = (temp1+temp2+carry)//10

            sum= str(temp)+sum
            if(digits == 0 and carry!=0):
                sum = str(carry)+sum

     
     
    print(sum)
     

main()