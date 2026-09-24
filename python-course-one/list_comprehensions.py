List comprehension in Python


numbers = list(range(10))
doubled_numbers = [n*2 for n in numbers]

phrases = [f'Iam{age} years old' for age in doubled_numbers]

print(phrases)

names_list = ['John', 'Rolf', 'Anne']
lowercase_names = [name.lower() for name in names_list]

print(lowercase_names)

friends = input("Enter your friends names: ")
print(friend.lower() in lowercase_names)

## with conditional

evens = [n for n in numbers if n % 2 == 0]
print(evens)


friends = ['john', 'rolf', 'anne']
guests = ['John', 'Rolf', 'Job', 'Mary', 'Bob']

present_friends = [friend.capitalize() for friend in friends if friend.lower() in guests]

print(present_friends)
