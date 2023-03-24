def prime_checker(number):
    count = 0
    if number == 1:
        print("1 is not prime number")
    else:
        for i in range(1,number+1):
            if number % i == 0:
                count += 1
            else:
                pass
        if count == 2:
            print("It's a prime number.")
        else:
            print("It's a not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)


