#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i, end=" ")

        '''if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")'''
