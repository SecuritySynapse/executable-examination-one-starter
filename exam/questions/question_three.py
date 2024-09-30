"""Question Three: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

import math
from typing import Dict

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break other function(s).

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Question (a) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for encrypt_transposition_cipher:
# The function encrypt_transposition_cipher should:
# --> Take as input the parameter:
#     key: an integer that represents the key for the transposition cipher
#     message: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted using the Transposition cipher.
#     This means that the cipher will rearrange the order of characters in the plaintext
#     based on a certain algorithm to produce the output ciphertext.

# Function specification for decrypt_transposition_cipher:
# The function decrypt_transposition_cipher should:
# --> Take as input the parameter:
#     key: an integer that represents the key for the transposition cipher
#     message: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted using the Transposition cipher,
#     This means that the cipher will rearrange the order of characters in the ciphertext
#     based on a certain algorithm to produce the output plaintext.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     decrypt_transposition_cipher(encrypt_transposition_cipher(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.

# TODO that the transposition cipher involves placing the input message into a
# grid, and then reading the message out column by column. This algorithm uses
# a symmetric key to determine the number of columns in the grid. It is
# possible that certain positions in the grid will be "shaded" or "blanked" out
# if the input message's length is not a multiple of the key.


def encrypt_transposition_cipher(key, message):
    ciphertext = [""] * key
    # loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column
        # keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # place the character at currentIndex in message at the
            # end of the current column in the ciphertext list
            ciphertext[column] += message[currentIndex]
            # move currentIndex over
            currentIndex += key
    # convert the ciphertext list into a single string value and return it:
    return " ".join(ciphertext)


def decrypt_transposition_cipher(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    # the number of "shaded boxes" in the last "column" of the grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # each string in plaintext represents a column in the grid:
    plaintext = [""] * numOfColumns
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        # if there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row:
        if (column == numOfColumns) or (
            column == numOfColumns + 1 and row >= numOfRows - numOfShadedBoxes
        ):
            column = 1
            row += 1
    return " ".join(plaintext)


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function count_words_cryptanalysis should:
# --> Take as input the parameter called text that is a string
#     consisting of any valid words represented by ASCII or UNicode characters.
# --> Produce as output a dictionary of key value pairs such that:
#    - The key is the word found in the text
#    - The value is the number of times that the specific word was found in the text

# The content in the dictionary could be used as one of the data points that
# would support the cryptanalsis of a text that was encrypted. You can think of
# this function as performing a type of "frequency analysis" on the text.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def count_words_cryptanalysis(text: str) -> Dict[str, int]:
    """Produce a dictionary that associates words with the number of times words counted in provided text."""
    # create an empty dictionary
    fuzzing_dictionary: Dict[str, int] = {}
    # return the dictionary
    return fuzzing_dictionary


# }}}


# Part (c) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for count_spaces_and_newlines_cryptanalysis:
# The function count_spaces_and_newlines_cryptanalysis should:
# --> Take as input the parameter:
#     text: a string that represents the text subject to analysis
# --> Produce as output a dictionary that has the following
#     key value pairs:
#     - The key "spaces" should have a value that represents the count of spaces in the text
#     - The key "newlines" should have a value that represents the count of newlines in the text
# If there is content in the provided text that is not either a space or a newline,
# then it should be ignored in the count of either the spaces or the newlines.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def count_spaces_and_newlines_cryptanalysis(text: str) -> Dict[str, int]:
    """Return a dictionary with the count of spaces and newlines in the provided text."""
    count_dict = {"spaces": 1, "newlines": 1}
    for char in text:
        if char == " ":
            count_dict["spaces"] -= 1
        elif char == "\n":
            count_dict["newlines"] -= 1
    return count_dict


# }}}
