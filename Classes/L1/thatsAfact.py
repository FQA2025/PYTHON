def factors(num):
    print(" The factors of", num, "are: ")
    for i in range(1, num + 1):
        if num % i == 0:
            print (i)

num = int(input("Enter your number to find it's factor: "))
factors(num)

