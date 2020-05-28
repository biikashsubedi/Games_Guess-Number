from random import randint
import sys
import argparse

args = argparse.ArgumentParser("python3 randomgame.py -s START -e END")
args.add_argument('-s', '--start', default=0)
args.add_argument('-e', '--end', default=10)

options = args.parse_args()
print("Start: ", options.start)
print("End: ", options.end)

#generate a number
answer = randint(int(options.start), int(options.end))

#input the number
# guess = input("Enter the number that on ur mind 1~10: ")
#check the number between 1-10
while True:
    try:
        guess = int(input(f"Guess a Number between {options.start}~{options.end}: "))
        if guess>int(options.start) and guess<int(options.end):
            if guess == answer:
                print('You are Genious!!')
                break
        else:
            print(f"Hey beb, i said between {options.start}~{options.end}")
    except ValueError:
        print(f"Please Choose NUmber Between {options.start}~{options.end} ")
        continue



