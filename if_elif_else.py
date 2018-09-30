#demo program to understand if elif else
#program to check greatest among three number
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if (num1 > num2) & (num1 > num3):
    print('num1 is greater')
elif (num2 > num1) & (num2 > num3):
    print('num2 is greater')
else:
    print('num3 is greater number')



