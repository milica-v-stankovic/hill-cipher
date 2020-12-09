from HillCipher import hillCipher

hc = hillCipher.HillCipher([[17, 17, 5], [21, 18, 21], [2, 2, 19]], 30, 3)

word = hc.cipher("CONTIGOHASTAELFINAL")

print(word)