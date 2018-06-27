def reverse_sentence(sentence):
    sentence = sentence.rstrip().lstrip()
    wordArray = sentence.split()
    reversedSentence =""

    for word in wordArray[::-1] :
        reversedSentence += ' ' +  word

    return reversedSentence.lstrip()


