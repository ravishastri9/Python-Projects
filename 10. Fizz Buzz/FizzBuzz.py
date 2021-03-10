"The program will print 'fizz' and 'Buzz' for numbers divisible by 3 and 5 and 'FizzBuzz' for numbers divisible by both."


for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
