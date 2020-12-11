from HillCipher.key import Key

class HillCipher(object):
    
    def __init__(self, key, modulo, blockSize):
        self.key = Key(key, modulo, blockSize)
        self.blockSize = blockSize

    def cipher(self, word):
        keyValid = self.key.checkKeyValidity()

        if keyValid == False:
            return False, None

        key = self.key.returnKeyValue()

        cipherText = self.__transformText(key, word)
        
        return True, cipherText

    def decipher(self, word):
        keyValid = self.key.checkKeyValidity()

        if keyValid == False:
            print("Invalid key! Exiting...")
            return False, None

        key = self.key.getInverseKey()
        

        originalText = self.__transformText(key, word)

        originalText = originalText.replace("?", "")
        
        return True, originalText


    def __transformText(self, key, word):
        numericText = []
        cipherText = ""

        for i in range(0, len(word), self.blockSize):
            textBlock = self.__getWordBlock(word, i)
            numericKeyBlock = self.__convertTextToNumberArray(textBlock)
            cipherBlock = self.__cryptWordBlock(numericKeyBlock, key)
            numericText[i:i+self.blockSize] = cipherBlock
        cipherText = self.__convertNumberArrayToText(numericText)

        return cipherText


    def __cryptWordBlock(self, wordBlock, key):

        cipherArray = []
        for i in range(self.blockSize):
            cipherArray.append(0)
            for j in range(self.blockSize):
                cipherArray[i] += key[i][j] * wordBlock[j]
            cipherArray[i] = cipherArray[i] % self.key.modulo
        
        return cipherArray

    def __getWordBlock(self, word, startPosition):

        endPosition = 0

        if (startPosition + self.blockSize <= len(word)):
            endPosition = startPosition + self.blockSize
        else:
            endPosition = (startPosition + self.blockSize) + (startPosition + self.blockSize - len(word))
            for i in range (startPosition + self.blockSize - len(word)):
                word += '?'


        textBlock = word[startPosition:endPosition]
        return textBlock

    def __convertTextToNumberArray(self, text):
        numericArray = []
        for i in range(len(text)):
            numericArray.append(ord(text[i]) - 60)

        return numericArray

    def __convertNumberArrayToText(self, numberArray):
        text = ""

        for i in range(len(numberArray)):
            text += chr(numberArray[i] + 60)

        return text