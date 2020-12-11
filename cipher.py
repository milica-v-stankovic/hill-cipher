from HillCipher import hillCipher
import re

print("=========================")
print("HILL CIPHER")
print("=========================")

print()
print()
print()

print("Please enter the key file you would like to use: (default: keys/key.text)")

filename = input()

if filename == '':
    filename = "keys/key.txt"

with open(filename, "r") as file:
    key = [[int(num) for num in line.split(',')] for line in file]

    hc = hillCipher.HillCipher(key, 30, 3)

    print("Please enter the cipher word.")

    word = input()

    result = re.match('[A-Z]*', word)

    while result.span()[1] != len(word):
        print("Word must only contain the characters in [A-Z]!")
        print("Please re-enter the word")
        word = input()
        result = re.match('[A-Z]*', word)

    print("Result is:")
    word = hc.cipher(word)
    print(word[1])