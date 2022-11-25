#Write your code below this line 👇



def prime_checker(number):
    u = 0
    for i in range(1,101):
        if number % i == 0:
            u = u + 1 
        else:
            u = u + 0 
    if u == 2: 
        print(f"{number} is Prime number")
    else:
        print(f"{number} is not a Prime number")





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

