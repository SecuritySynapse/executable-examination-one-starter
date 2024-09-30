"""Question One: Executable Examination."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

import random

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

# Function specification for encrypt_caesar_cipher:
# The function encrypt_caesar_cipher should:
# --> Take as input the parameters:
#   - plaintext: a string that represents the plaintext to be encrypted
#   - shift: an integer that represents the shift to be applied
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted using a Caesar cipher with the provided shift,
#     This means that the cipher will take a letter in the plaintext and shift it
#     by the shift amount to produce that specific letter in the output ciphertext.

# Function specification for decrypt_caesar_cipher:
# The function decrypt_caesar_cipher should:
# --> Take as input the parameters:
#   - ciphertext: a string that represents the ciphertext to be decrypted
#   - shift: an integer that represents the shift to be applied
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted using a Caesar cipher with the provided shift,
#     This means that the cipher will take a letter in the ciphertext and shift it
#     by the shift amount in the opposite direction (of the encryption algorithm) to
#     produce that specific letter in the output plaintext.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     decrypt_caesar_cipher(encrypt_caesar_cipher(plaintext, shift), shift).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#    the encryption algorithm.


def encrypt_caesar_cipher(plaintext, shift = 3):
    """Encrypt the provided plaintext using a Caesar cipher with the provided shift."""
    result = ""
    return result


def decrypt_caesar_cipher(ciphertext, shift = 3):
    """Decrypt the provided ciphertext using a Caesar cipher with the provided shift."""
    result = ""
    return result


# }}}

# Part (b) {{{

# Instructions: Implement and/or debug the following function so that it
# adheres to all aspects of the following specification.

# Function specification:
# The function fuzzer should:
# --> Take as input the parameters:
#    - max_length: an integer that represents the maximum length of the string
#    - char_start: an integer that represents the starting character
#    - char_range: an integer that represents the range of characters
# --> Produce as output a string that is of a length that is less than or equal to max_length
# --> The output string will be a random string that may contain:
#    - symbols like punctuation marks
#    - symbols like spaces or dollar signs or percent signs
#    - numbers like 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def generate_fuzzer_value(
    max_length: int = 100, char_start: int = 32, char_range: int = 32
) -> str:
    """Make string of up to max_length characters in the range [char_start, char_start + char_range)."""
    string_length = random.randrange(0, max_length + 1)
    out = "[]"
    for _ in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out + "[]"


# }}}


# Part (c) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for reverse_string_encrypt:
# The function reverse_string_encrypt should:
# --> Take as input the parameter:
#     plaintext: a string that represents the plaintext to be encrypted
# --> Produce as output a string that represents the encrypted text
# --> The output string will be encrypted by reversing the order of the
#     characters in the plaintext.

# Function specification for reverse_string_decrypt:
# The function reverse_string_decrypt should:
# --> Take as input the parameter:
#     ciphertext: a string that represents the ciphertext to be decrypted
# --> Produce as output a string that represents the decrypted text
# --> The output string will be decrypted by reversing the order of the
#     characters in the ciphertext.

# The following property should hold for all inputs:
# --> The original plaintext should be equal to the output of
#     reverse_string_decrypt(reverse_string_encrypt(plaintext)).
# --> In other words, the decryption of the encryption of the plaintext
#     should be equal to the original plaintext.
# --> In other words, the decryption algorithm should "undo" or "reverse"
#     the encryption algorithm.

# TODO: Even though this is not considered an example of a useful cryptographic
# algorithm, it is still a suitable example of a way to associated the
# plaintext with the ciphertext during a cryptanalysis process for a more
# realistic cryptographic algorithm.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def reverse_string_encrypt(plaintext: str) -> str:
    """Encrypt the provided plaintext by reversing the order of its characters."""
    return ""


def reverse_string_decrypt(ciphertext: str) -> str:
    """Decrypt the provided ciphertext by reversing the order of its characters."""
    return ""


def reverse_string_encrypt_dictionary(plaintexts: list) -> dict:
    """Encrypt a list of plaintexts by reversing and returning a dictionary of data."""
    return {0: ""}

# }}}
