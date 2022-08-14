#Task 2

def ch_prime(number):
    if number > 1:
        for i in range(2 , int(number/2)+1):
            if number % i == 0:
                print(number, ":Not prime")
                break
        else:
            print(number, ':This is a prime')
ch_prime(8)
ch_prime(7)