import random
changes  = random.randit(1, 9)
number = input("Enter any nuber:")

while changes < 5:
    if guess == number:
        print('Congratulations you won!!')
        break
    if not changes < 5:
        print('You loose!! the number is' number)