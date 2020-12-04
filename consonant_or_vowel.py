# !/usr/bin/env Python3

# Created by Larry Nkengbeza
# Created on December 2020
# This program identifies letters as either consonant or vowel.


def main():
    # Input
    letter = str(input("Enter the letter: "))
    letter_a = ("a")
    letter_e = ("e")
    letter_i = ("i")
    letter_o = ("o")
    letter_u = ("u")
    # Process
    if letter == letter_a:
        print("The letter that you just enterd is a vowel.")
    elif letter == letter_e:
        print("The letter that you just enterd is a vowel.")
    elif letter == letter_i:
        print("The letter that you just enterd is a vowel.")
    elif letter == letter_o:
        print("The letter that you just enterd is a vowel.")
    elif letter == letter_u:
        print("The letter that you just enterd is a vowel.")
    else:
        print("The letter you just entered is a consonant.")


if __name__ == "__main__":
    main()
