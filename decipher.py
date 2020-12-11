from HillCipher import hillCipher
import re

print("=========================")
print("HILL DECIPHER")
print("=========================")

print()
print()
print()

print("Please enter the key file you would like to use: (eg. keys/key.text)")

filename = input()

if filename == '':
    filename = "keys/key.txt"

with open(filename, "r") as file:
    key = [[int(num) for num in line.split(',')] for line in file]

    hc = hillCipher.HillCipher(key, 30, 3)

    print("Please enter the cipher word.")

    cipherWord = input()

    result = re.match('[A-Z<=>?@]*', cipherWord)
    print(result.span())

    while result.span()[1] != len(cipherWord) or (len(cipherWord) % 3 != 0):
        print("Word must only contain the characters in [A-Z] or characters in [<, =, >, ?, @] and its size must be divisible by 3!")
        print("Please re-enter the word")
        cipherWord = input()
        result = re.match('[A-Z<=>?@]*', cipherWord)

    print("Result is:")
    word = hc.decipher(cipherWord)
    print(word[1])