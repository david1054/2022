import random

user = input("Heads or Tails?\n")
options = [1, 2]
heads_tails = random.choice(options)

if heads_tails == 1:
    print("It's heads!")
else:
    print("It's tails!")


  