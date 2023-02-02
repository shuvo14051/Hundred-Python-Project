import random
# Generate a from 1 t0 10.
n = random.randrange(1,11)
guess = int(input("Enter any number: "))
count = 0
while True:
    # 
    count+=1
    if guess < n:
        print("Low")
        guess = int(input("Enter another number: "))

    elif guess > n:
        print("High")
        guess = int(input("Enter another number: "))

    else:
        print("You guessed it right!! The number was {} you guessed {}.".format(n,guess))
        print("You had tried {} times to reach the right number.".format(count))
        break