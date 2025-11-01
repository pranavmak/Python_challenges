import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

print("Welcome to the PyPassword generator !")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Password in fixed sequence i.e. letters, numbers and symbols
# password = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0,nr_numbers):
#     password += random.choice(numbers)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# print(password)

# Step 1: collect all chosen characters into a list
password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Step 2: shuffle the list to randomize order
random.shuffle(password_list)

# Step 3: join the shuffled list into a string
password = ''.join(password_list)


print(f"Your random password is: {password}")
