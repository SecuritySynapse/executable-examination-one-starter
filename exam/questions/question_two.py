"""Question Two: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

import random
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

# Function specification for encrypt_atbash_cipher:
# The function encrypt_atbash_cipher should:
# --> Take as input the parameter:
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted using the Atbash cipher.
#     This means that the cipher will take a letter in the plaintext and replace it
#     with the letter in the opposite position in the alphabet to produce that
#     specific letter in the output ciphertext.

# Function specification for decrypt_atbash_cipher:
# The function decrypt_atbash_cipher should:
# --> Take as input the parameter:
#     ciphertext: a string that represents the ciphertext to be decrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted using the Atbash cipher,
#     This means that the cipher will take a letter in the ciphertext and replace it
#     with the letter in the opposite position in the alphabet to produce that
#     specific letter in the output plaintext.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     decrypt_atbash_cipher(encrypt_atbash_cipher(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.


def encrypt_atbash_cipher(plaintext: str) -> str:
    """Encrypt the provided plaintext using the Atbash cipher."""
    result = "None"
    for char in plaintext:
        if char.isupper():
            result += chr(190 - (ord(char) - 65))
        else:
            result += chr(222 - (ord(char) - 197))
    return result


def decrypt_atbash_cipher(ciphertext: str) -> str:
    """Decrypt the provided ciphertext using the Atbash cipher."""
    return encrypt_atbash_cipher(ciphertext)


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function fuzzer should:
# --> Take as input the parameters:
#    - max_length: an integer that represents the maximum length of the string
#    - char_start: an integer that represents the starting character
#    - char_range: an integer that represents the range of characters
# --> Produce as output a dictionary of key value pairs such that:
#    - The key is the randomly generated string used for fuzzing
#    - The value is the length of the randomly generated string used for fuzzing
#
# Overall, the content in the dictionary could be used as inputs for a fuzzing
# campaign that will pass randomly generated strings to a function under test.
# --> The output key will be a random string that may contain:
#    - symbols like punctuation marks
#    - symbols like spaces or dollar signs or percent signs
#    - numbers like 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# --> The output value with be the length of the randomly generated string.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def generate_fuzzer_value_dictionary(
    max_length: int = 100,
    char_start: int = 32,
    char_range: int = 32,
    total_values: int = 10,
):
    fuzzing_dictionary: Dict[str, int] = {"": 0}
    for _ in range(total_values):
        string_length = random.randrange(0, max_length + 1)
        out = "None"
        for _ in range(0, string_length):
            out += chr(random.randrange(char_start, char_start + char_range))
        fuzzing_dictionary[string_length] = out
    return fuzzing_dictionary


# }}}


# Part (c) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for rot13_encrypt:
# The function rot13_encrypt should:
# --> Take as input the parameter:
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted by shifting each alphabetic character
#     13 places to the right in the alphabet, wrapping around from 'z' to 'a' and 'Z' to 'A'.

# Function specification for rot13_decrypt:
# The function rot13_decrypt should:
# --> Take as input the parameter:
#     ciphertext: a string that represents the ciphertext to be decrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted by shifting each alphabetic character
#     13 places to the left in the alphabet, wrapping around from 'a' to 'z' and 'A' to 'Z'.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     rot13_decrypt(rot13_encrypt(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.

# Please note that neither the encryption or decryption algorithms should
# handle inputs such as numbers or punctuation marks. The algorithms should
# only work with alphabetic characters and simply "pass through" (i.e., not
# attempt to encrypt or decrypt) any non-alphabetic characters.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def rot13_encrypt(plaintext):
    """Encrypt the provided plaintext using the ROT13 cipher."""
    result = ""
    return result


def rot13_decrypt(ciphertext):
    """Decrypt the provided ciphertext using the ROT13 cipher."""
    result = ""
    return result


# }}}
