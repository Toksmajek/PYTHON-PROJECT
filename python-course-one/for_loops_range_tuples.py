# Python course: for loops, range(), and tuple unpacking
# Starter examples for the next lesson.

# 1. A for loop visits each item in a collection.
languages = ["Python", "JavaScript", "Java"]
for language in languages:
    print(language)

# 2. range(start, stop) includes start but excludes stop.
for number in range(1, 6):
    print(number)  # 1, 2, 3, 4, 5

# Add a step to count in twos.
for number in range(0, 10, 2):
    print(number)  # 0, 2, 4, 6, 8

# 3. Tuple destructuring (unpacking) assigns values to separate names.
student = ("Alex", 25)
name, age = student
print(name, age)

# Unpack each tuple directly in a for loop.
students = [("Alex", 25), ("Sam", 30), ("Jo", 22)]
for name, age in students:
    print(f"{name} is {age} years old.")

# Practice:
# - Print numbers 1 through 10 using range().
# - Add another student to the list and run the loop again.
# Write your own code below:
primes = {2,3,5,7,11} 

for prime in primes:
    print(f'{prime} is a prime number.')



kid_ages = (3, 7, 12)
for age in kid_ages: 
    print(f'Ihave a {age} year old kid. ')


for i in range(20):
    print(i)


my_friends = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22
}

for name, days in my_friends.items()
    if name == "Bob":
        print('I know Bob!')
    print(f"I last saw {name} {days} days ago. ")
    print(f"I last saw {name} {days} days ago. ") 


print(my_friends.items()) # [('alice', 25), ('Bob', 30), ('Charlie', 22)]

for t in [("Alice", 25), ("Bob", 30), ("Charlie", 22)]:
    n, v = t
    print(n)
    print(v)

who_do_i_know = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
if who_do_i_know in my_friends: 
    print("I know them!")