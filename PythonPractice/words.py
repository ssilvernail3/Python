# words = ['Arlo', 'Dexter', 'Shane','Ally']


def print_upper_words(words):
    ''' This function takes a list of words and prints them out individually in Uppercase'''

    for word in words:
        print(word.upper())


print_upper_words(['hello', 'Shane', 'Ally'])


def print_upper_words2(words):
    ''' This function takes a list of words and prints out the ones starting with the letter 'e' '''

    for word in words:
        if word.startswith('e'):
            print(word)


print_upper_words2(['hello', 'Shane', 'Ally', 'electric', 'economy'])


def print_upper_words3(words, must_start_with):
    '''This function takes a list of words and prints them out individually in Uppercase'''

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word)
                break


print_upper_words3(['hello', 'Shane', 'Ally', 'electric', 'economy'], 'a')
