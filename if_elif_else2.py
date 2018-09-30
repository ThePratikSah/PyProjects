#   program to check a number is positive , negative and zero

year = int(input('enter any year: '))
if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print('not a leap year')
elif year % 4 == 0:
    print('leap year')
else:
    print('not a leap year')

