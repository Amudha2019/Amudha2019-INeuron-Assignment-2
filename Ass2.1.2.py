#Write a function filter_long_words() that takes a list of words and
#an integer n and returns the list of words that are longer than n.

def filter_long_words(inputList,inputInteger):

    listOfWords = []

    for i in range(len(inputList)):
        if len(inputList[i]) > inputInteger:
            listOfWords.append(inputList[i])

    return listOfWords

inputListOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']
inputWordLength = 7

print (str(filter_long_words(inputListOfWords,inputWordLength)))
