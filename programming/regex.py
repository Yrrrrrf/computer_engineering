'''
Regular Expression (RegEx)
Is a sequence of characters that define a search pattern, used to perform pattern-matching and "search-and-replace" functions on text.
'''


import re  # regular expression


def main() -> None:
    '''App Entry Point'''
    # regex examples
    # match() - returns a match object if there is a match anywhere in the string
    # search() - returns a match object if there is a match anywhere in the string
    # findall() - returns a list containing all matches
    # split() - returns a list where the string has been split at each match
    # sub() - replaces one or many matches with a string

    text = 'The rain in Spain'
    pattern = re.compile(r'ain')  # r - raw string
    # pattern = re.compile(r'ain', re.IGNORECASE)
    print(pattern.findall(text))  # ['ain', 'ain']


    pass


if __name__ == '__main__':
    main()
