Functions, arguments, and parameters in Python


# name = input('Enter your name: ')
# print(f'Hello, {name}')

def greet_user(name):
    name = input('Enter your name: ')
    print(f'Hello, {name}')

print('Before the function')

greet_user('John')  # Calling the function with an argument

print('Hello')



def check_if_prime(n): #number is a parameter
for n in range(2, 10): #[2, 3, 4, 5, 6, 7, 8, 9]  
    for x in range(2, n): #[], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8]  
        if n % x == 0:  
            print(f'{n} equals {x} * {n//x}')  
            break  
    else:  
        # loop fell through without finding a factor  
        print(f'{n} is a prime number')


for n in range(2, 10): 
  check_if_prime(n)  # n is called an argument here, because it is being passed to the function check_if_prime



check_primes(200)  # This will check for prime numbers from 2 to 200 ta