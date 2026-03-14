import random
import string
print("PASSWORD GENERATOR")
name = input("enter your name:")
phone = input("enter your phone model:")
length = int(input("enter your password length:"))
letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*"
all_characters = letters+ numbers + symbols
password =""
for i in range(length):
    password+=random.choice(all_characters)
    print("generated password:",password)