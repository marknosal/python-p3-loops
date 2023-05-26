#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i > 0):
        print(i)
        i -= 1
    print('Happy New Year!')


def square_integers(int_list):
    int_list = [data_point * data_point for data_point in int_list]
    return int_list
    



def fizzbuzz():
    i = 1
    while (i <= 100):
        if i % 3 == 0:
            if i % 5 == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i += 1

fizzbuzz()