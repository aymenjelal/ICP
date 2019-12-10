def theater(n,m,a):
    if(n%a==0):
        i = n//a
    else:
        i = (n//a)+1

    if(m%a==0):
        j = m//a
    else:
        j = (m//a)+1
    
    return i*j


if __name__== '__main__':
    inputs=input().split(" ")
    n=int(inputs[0])
    m=int(inputs[1])
    a=int(inputs[2])
    
    print(theater(n,m,a))
    