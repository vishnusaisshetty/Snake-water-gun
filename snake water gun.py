import random

options = ["snake", "water", "gun"]
random = random.sample(options, k=1)[0].strip()
print(random)
while True:
    user = input(f"Enter your choice {options} :" )
    if (random == user):
        print("try again")
        print(f"computer choice is:{random}")
        break
    elif (user == "snake" and random == "water") or\
        (user == "water" and random == "gun") or \
        (user == "gun" and random == "snake"):
        print("You won!")
        break
    else:
        print("Computer won")
        break
