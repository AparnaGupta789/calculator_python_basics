print('enter 1st no: ')
a=int(input())
print('enter the operation you want to perform')
c=input()
print('enter 2nd no: ')
b=int(input())
if(c=='*'):
    print(a*b)
elif(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='/'):
    print(a/b)
elif(c=='//'):
    print(a//b) 
elif(c=='**'):
    print(a**b) 
elif(c=='%'):
    print(a%b)
else:
    print('unknown operation')
