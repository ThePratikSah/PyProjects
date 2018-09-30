choice = int(input('1: weight'
      '\n2: length'
      '\n3: Temp'
      '\n4: memory'
      '\n5: area'
      '\n\nEnter your choice: '))

#   creating a program for weight conversion
if choice == 1:
    weight = int(input('1: kg to gm'
                       '\n2: gm to kg'
                       '\nEnter your choice: '))
    if weight == 1:
        kg = int(input('Enter your weight in kg: '))
        print('value in gm: ',kg * 1000)
    elif weight == 2:
        gm = int(input('Enter your weight in gm: '))
        print('value in kg: ',gm / 1000)
    else:
        print('Invalid choice')


# creating program for length conversion
elif choice == 2:
    length = int(input('1: km to m'
                       '\n2: m to km'
                       '\nEnter your choice: '))
    if length == 1:
        km = int(input('Enter your length in km: '))
        print('value in m: ',km * 1000)
    elif length == 2:
        m = int(input('Enter your length in m: '))
        print('value in km: ',m / 1000)
    else:
        print('Invalid choice')
#  creating program for temp conversion.
elif choice == 3:
    temp = int(input('1: C to F'
                     '\n2: F to C'
                     '\nEnter your choice: '))
    if temp == 1:
        cel = float(input('Enter your temp in celcius: '))
        print('temp in cel: ',((9/5)*(cel + 32)))
    elif temp == 2:
        far = float(input('Enter your temp in farenheit: '))
        print('temp in far: ',((5/9)*(far - 32)))
    else:
        print('Invalid choice')


#   creating program for memory conversion.
elif choice == 4:
    memory = int(input('1: kb to mb'
                     '\n2: mb to kb'
                     '\nEnter your choice: '))
    if memory == 1:
        kb = int(input('Enter your memory in kb: '))
        print('memory in mb: ',kb / 1024)
    elif memory == 2:
        mb = int(input('Enter your memory in mb: '))
        print('memory in kb: ',mb * 1024)
    else:
        print('Invalid choice')


# creating program for area.
elif choice == 5:
    area = int(input('1: rectangle'
                     '\n2: square'
                     '\n3: circle'
                     '\nEnter your choice: '))
    if area == 1:
        length = int(input('Enter the length of rectangle: '))
        width = int(input('Enter the width of rectangle'))
        print('area: ',length * width)
    elif area == 2:
        side = int(input('Enter the side of square: '))
        print('area of square: ',side * side)
    elif area == 3:
        radius = int(input('Enter the radius of circle: '))
        print('area of circle: ', 3.14 * radius ** 2)
    else:
        print('Invalid choice')

# my first 85 line of program







