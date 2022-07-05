#Program to find the factorial of a number

num = int(input('Enter the number:'))
fact = 1

if(num < 0):
    print('The entered number is less than zero')
elif(num == 0):
    print('The factorial of {0} is: 1'.format(num))
else:
    for i in range(1,num+1):
        fact = fact * i
    print('Factorial of {0} is: {1}'.format(num,fact))

