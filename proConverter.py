import os


def cls():
    os.system("clear")


def flow():
    option = input('Would you like to have a new conversion?(y/n)')
    if option == 'y':
        menu()
    elif option == 'n':
        exit()
    else:
        print('Invalid choice. Try again!')


def menu():
    print('What would you like to convert? Choose an option below.\n\n1. Temperature conversion'
          '\n2. Memory conversion'
          '\n3. Weight conversion'
          '\n4. Distance conversion'
          '\n5. Time conversion'
          '\n6. Area conversion'
          '\n7. No thanks, Let me exit.')
    option = int(input('\nEnter your choice: '))

    if option == 1:
        temp()
    elif option == 2:
        memory()
    elif option == 3:
        weight()
    elif option == 4:
        distance()
    elif option == 5:
        time()
    elif option == 6:
        area()
    elif option == 7:
        print('Sorry to see you go. Take care. Bye!')
        exit()
    else:
        print('Invalid choice. Try again!')
        menu()


def message():
    print('Welcome to the Pro Calculator. I\'m Calc, your personal conversion assistant.')
    name = input('Please enter your name so that I can guide you further. \nYour name: ')
    cls()
    print('Hello {}, Thanks for choosing me as your new friend, Let\' get started.'
          .format(name))
    menu()


def temp():
    choice = int(input('1. F to C \n2. C to F \nEnter your choice: '))
    if choice == 1:
        f = float(input('Enter your temperature in F: '))
        c = (5 / 9) * (f - 32)
        print('On converting {} into C, we get {}'.format(f, c))
        flow()
    elif choice == 2:
        c = float(input('Enter your choice in C: '))
        f = (9 / 5) * c + 32
        print('On converting {} into F, we get {}'.format(c, f))
        flow()
    else:
        print('Invalid Choice, Try again!')
        temp()


def memory():
    choice = int(input('1. KB to MB \n2. MB to GB \n3. GB to TB \n4. Return to menu. '
                       '\nEnter your choice: '))
    cls()
    if choice == 1:
        kb = int(input('Enter the value in KB: '))
        print('The value of {} KB is {} MB.'.format(kb, kb / 1024))
        flow()
    elif choice == 2:
        mb = int(input('Enter the value in MB: '))
        print('The value of {} MB is {} GB.'.format(mb, mb / 1024))
        flow()
    elif choice == 3:
        gb = int(input('Enter the value in GB: '))
        print('The value of {} GB is {} TB.'.format(gb, gb / 1024))
        flow()
    elif choice == 4:
        menu()
    else:
        print('Invalid choice. Try again!')
        memory()


def weight():
    choice = int(input('1. Gram to Kg \n2. Kg to gram \nEnter your choice: '))
    if choice == 1:
        gm = int(input('Enter the weight in gram: '))
        print('On converting {} gram into kg, we have {}'.format(gm, gm / 1000))
        flow()
    elif choice == 2:
        kg = int(input('Print the weight in kg: '))
        print('On converting {} kg into gram, we have {}'.format(kg, kg * 1000))
        flow()
    else:
        print('Invalid choice, Try again!')
        weight()


def distance():
    choice = int(input('1. Meter to KM \n2. KM to meter \nEnter your choice: '))
    if choice == 1:
        m = float(input('Enter your distance value in meter: '))
        print('On converting {} meter into KM, we get {}'.format(m, m / 1000))
        flow()
    elif choice == 2:
        km = float(input('Enter your distance value in KM: '))
        print('On converting {} KM into meter, we get {}'.format(km, km * 1000))
        flow()
    else:
        print('Invalid choice, Try again!')
        distance()


def time():
    choice = int(input('1. sec to minute \n2. minutes to hour \nEnter your choice: '))
    if choice == 1:
        sec = int(input('Enter your time in seconds: '))
        print('On converting {} seconds into KM, we get {}'.format(sec, sec / 60))
        flow()
    elif choice == 2:
        minute = int(input('Enter your time in minutes: '))
        print('On converting {} minutes into hour, we get {}'.format(minute, minute * 60))
        flow()
    else:
        print('Invalid choice, Try again!')
        time()


def area():
    choice = int(input('1. Rectangle'
                       '\n2. Square'
                       '\n3. Circle'
                       '\nEnter your choice: '))
    if choice == 1:
        leng = int(input('Enter the length of rectangle: '))
        bre = int(input('Enter the width of rectangle: '))
        print('Area of the given rectangle is: {}'.format(leng * bre))
        flow()
    elif choice == 2:
        side = int(input('Enter the side of square: '))
        print('Area of a square is: {}'.format(side * side))
        flow()
    elif choice == 3:
        radius = int(input('Enter the radius of the circle: '))
        print('Area of the circle is: {}'.format(3.14 * radius * radius))
        flow()
    else:
        print('Invalid choice, Try again!')
        area()


if __name__ == '__main__':
    message()
