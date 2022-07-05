#program to check if the entered number is even or odd

num = int(input('Enter the number:'))

if(num % 2 == 0):
    print("{0} is an even number".format(num))
else:
    print("{0} is an odd number".format(num))
