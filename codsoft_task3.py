import random

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
len = int(input("\nEnter the length of password: "))

password = "".join(random.sample(char,len))

print("Your new Password is:",password)