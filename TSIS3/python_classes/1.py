class met:

    def getString(self, text):
        return text
    def printSring(self, text):
        print(self.getString(text).upper())

som = met()
som.printSring(som.getString(input()))
