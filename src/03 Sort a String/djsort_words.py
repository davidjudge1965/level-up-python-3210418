def sort_words(words):
    wordlist = words.split()
    #print (wordlist)
    sorted_strings = sorted(wordlist, key=str.lower)
    #print(sorted_strings)
    return sorted_strings

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE