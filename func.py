#   prime function
def prime(num):
    flag = 0
    for i in range(2, num // 2):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        print('Prime number.')
    else:
        print('Not a prime number.')


prime(123)


#   leap year
def leap(year):
    if year % 400 == 0:
        print('Leap year')
    elif year % 100 == 0:
        print('Not a leap year')
    elif year % 4 == 0:
        print('Leap year')
    else:
        print('Not a leap year')


leap(2012)


#   fact
def fact(num):
    ans = 1
    for i in range(1, num + 1):
        ans *= i
    print(ans)


fact(5)


#   sum of n number
def sum_of_n(num):
    sm = 0
    for i in range(1, num + 1):
        sm += i
    print(sm)


sum_of_n(30)


#   greater number in a list
def greater_num_in_list(list_var):
    print('Greatest number is', max(list_var))
    print('Smallest number is', min(list_var))


greater_num_in_list([3, 4, 6, 1, 0])


#   greater among three numbers
def greatest_among_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print('Num 1 is greatest')
    elif num2 > num1 and num2 > num3:
        print('Num 2 is greatest')
    else:
        print('Num 3 is greatest')


greatest_among_three(34, 5, 12)


#   reverse number
def reverse(num):
    ans = 0
    while num != 0:
        rem = num % 10
        ans = ans * 10 + rem
        num = num // 10
    print(ans)


reverse(435)


#   palindrome
def palindrome(num):
    ans = 0
    temp = num
    while num != 0:
        rem = num % 10
        ans = ans * 10 + rem
        num = num // 10
    if ans == temp:
        print('Palindrome')
    else:
        print('Not palindrome')


palindrome(323)


#   armstrong
def armstrong(num):
    flag = num
    arms = 0
    while num != 0:
        rem = num % 10
        arms = arms + rem ** 3
        num //= 10
    if arms == flag:
        print('Armstrong number')
    else:
        print('Not an armstrong number')


armstrong(153)

