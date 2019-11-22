# while loop, while loop with else, guessing game, car game, for loop
i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")

# guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_num = int(input("Guess: "))
    guess_count += 1
    if secret_number == guess_num:
        print("You Won!!")
        break
else:
    print("You Failed")

# car game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped...")
    elif command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quite
            ''')
    elif command == "quit":
        break
    else:
        print("I don't understand that...")

# for loops
for item in 'Python':
    print(item)

# for loops 2
for item in ['Minal', 'Test', 'Test 2']:
    print(item)

# for loop 3 to calculate total cost of the items
prices = [10, 20, 30]
total_price = 0
for price in prices:
    total_price += price
print(f"Total : {total_price}")





