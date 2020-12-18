#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# random letter
password = ""
for letter in range(nr_letters):
	# password += random.choice(letters)
	random_char = random.choice(letters)
	password += random_char

# random symbol
for symbol in range(nr_symbols):
	random_symbol = random.choice(symbols)
	password += random_symbol

# random number
for number in range(nr_numbers):
	random_num = random.choice(numbers)
	password += random_num

print(f"Your Random Password is: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# solution 1
l = list(password)
random.shuffle(l)
new_result = "".join(l)
print(f"Your Random Password is: {new_result}")

# solution 2
new_result_2 = "".join(random.sample(password, len(password)))
print(f"Your Random Password is: {new_result_2}")