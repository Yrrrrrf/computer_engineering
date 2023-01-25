# 
def get_first_letter(words_list: list[str]) -> list:
    """Returns a list with the first letter of each word in the list"""
    first_letters = []
    for word in words_list:
        try:
            assert type(word) == str, f'{word} is not a string'  # Asserts that the word is a string
            assert len(word) > 0, 'No words in the list'  # Asserts that the word is not empty
        except AssertionError as error:  # If the assertion fails, print the error
            print(error)
        first_letters.append(word[0].upper())  # Append the first letter (on uppercase) of the word to the list
    return first_letters


def run():
    print(get_first_letter(['hello', 'world', 'from', 'python', 'siuuuuuuuu']))

if __name__ == '__main__':
    run()

