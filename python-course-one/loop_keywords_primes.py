Two important loop Keywords + finding prime numbers

cars = ['ok', 'ok', 'faulty', 'ok'

for car_status in cars: 
    print(f' This car is {car_status}.')


if car_status == 'faulty':
    print('Stopping the production line!.')
    break


for num in range(2, 10):
    if num % 2== 0:
        print(f'found an even number, {num}')
        continue
    print(f'found a number, {num}')


for n in range(2, 10): #[2, 3, 4, 5, 6, 7, 8, 9]  
    for x in range(2, n): #[], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8]  
        if n % x == 0:  
            print(f'{n} equals {x} * {n//x}')  
            break  
    else:  
        # loop fell through without finding a factor  
        print(f'{n} is a prime number')
    
   