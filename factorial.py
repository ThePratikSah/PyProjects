num = int(input("Enter any number: "))
fact = 1
if num < 0:
    print("Factorial of negative number is not possible.")
elif num == 1:
    print("Factorial of 1 is 1.")
else:
    for i in xrange(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)
