#Password Generator Project
import random

password_List = []

letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
print(letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = random.randint(8, 10)
print(f"Number of letters in your password will be {nr_letters}")
nr_symbols = random.randint(2, 4)
print(f"Number of symbols in your password will be {nr_symbols}")
nr_numbers = random.randint(2, 4)
print(f"Number of numbers in your password will be {nr_numbers}")


#for loop to pick randomly from letters, symbols and numbers lists
for char in range(nr_numbers):
    password_List += random.choice(numbers) # += means add to the password_list
    print(f"Password Now is {password_List}")

for char in range(nr_letters):
    password_List += random.choice(letters)
    print(f"Password Now is {password_List}")

random.shuffle(password_List)

password = ""
for char in password_List:
    password += char
print(f"Your password is: {password}")
