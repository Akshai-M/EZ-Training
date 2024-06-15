def prime_number(num):
    if num >= 1:
        for i in range(2, (num//2) + 1 ):
            if (num % i) == 0:
                return False
        return True
    else:
        return False



def next_prime_number(num):
    if prime_number(num)  == False:
        print(num, "is not a prime number so cant continue")
        
        return

    list_of_prime = []
    for i in range(num+1, num+50):
        if prime_number(i):
            list_of_prime.append(i)
            # print(i)
        
    print(f"Level1: {list_of_prime[0]} is next prime number to {num}.")
    print(f"Level3: {list_of_prime[1]} is prime number next to {list_of_prime[0]}.")
    
    

num = int(input("Enter a number: "))
if prime_number(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

next_prime_number(num)