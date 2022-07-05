#program to find the sum of N natural numbers

num = int(input('Enter the number:'))

sum_num = 0

for i in range(1,num+1):
    sum_num = sum_num + i

print('Sum of {0} natural numbers is: {1}'.format(num,sum_num))
