def fizz_buzz(a):
    if a % 3 == 0:
        if a % 5 == 0:
            x = "FizzBuzz"
        else:
            x = "Fizz"
    elif a % 5 == 0:
        x = "Buzz"
    else:
        x = a
    return x

for i in range(100):
    print(fizz_buzz(i+1))