from HillCipher import hillCipher

print("=========================")
print("HILL DECIPHER")
print("=========================")

print()
print()
print()

print("Please enter the key file you would like to use: (eg. keys/key.text)")

filename = input()

with open(filename, "r") as file:
    key = [[int(num) for num in line.split(',')] for line in file]

    hc = hillCipher.HillCipher(key, 26, 3)

    word = hc.decipher("ZVTVTMTEQFSWUXVTMQRKL")

    print(word)