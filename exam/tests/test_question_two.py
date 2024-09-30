"""Confirm the correctness of functions in question_two."""

import pytest

# ruff: noqa: PLR2004
from questions.question_two import (
    decrypt_atbash_cipher,
    encrypt_atbash_cipher,
    generate_fuzzer_value_dictionary,
    rot13_decrypt,
    rot13_encrypt,
)


@pytest.mark.question_two_part_a
def test_encrypt_atbash_cipher():
    """Confirm correctness of question part."""
    assert (
        encrypt_atbash_cipher("ABC") == "ZYX"
    ), "Failed to shift forwards uppercase letters"
    assert (
        encrypt_atbash_cipher("abc") == "zyx"
    ), "Failed to shift forwards lowercase letters"
    assert (
        encrypt_atbash_cipher("XYZ") == "CBA"
    ), "Failed to shift backwards uppercase letters"
    assert (
        encrypt_atbash_cipher("xyz") == "cba"
    ), "Failed to wrap around lowercase letters"
    assert (
        encrypt_atbash_cipher("AbC") == "ZyX"
    ), "Failed to shift forwards mixed case letters"
    assert (
        encrypt_atbash_cipher("ZyX") == "AbC"
    ), "Failed to shift backwards mixed case letters"


@pytest.mark.question_two_part_a
def test_decrypt_atbash_cipher():
    """Confirm correctness of question part."""
    assert (
        decrypt_atbash_cipher("ABC") == "ZYX"
    ), "Failed to shift forwards uppercase letters"
    assert (
        decrypt_atbash_cipher("abc") == "zyx"
    ), "Failed to shift forwards lowercase letters"
    assert (
        decrypt_atbash_cipher("XYZ") == "CBA"
    ), "Failed to shift backwards uppercase letters"
    assert (
        decrypt_atbash_cipher("xyz") == "cba"
    ), "Failed to wrap around lowercase letters"
    assert (
        decrypt_atbash_cipher("AbC") == "ZyX"
    ), "Failed to shift forwards mixed case letters"
    assert (
        decrypt_atbash_cipher("ZyX") == "AbC"
    ), "Failed to shift backwards mixed case letters"


@pytest.mark.question_two_part_b
def test_generate_fuzzer_values():
    """Confirm correctness of question part."""
    total_values = 10
    result = generate_fuzzer_value_dictionary(max_length=10, total_values=10)
    assert len(result) == total_values, "Incorrect number of keys in the dictionary"
    for key, value in result.items():
        assert len(key) == value, "Length of the key does not match the value"
    char_start = 65
    char_range = 26
    result = generate_fuzzer_value_dictionary(10, char_start, char_range, 10)
    for current_key in result.keys():
        for char in current_key:
            assert (
                char_start <= ord(char) < char_start + char_range
            ), "Character is not in range"
    result = generate_fuzzer_value_dictionary(total_values=0)
    assert result == {}, "Dictionary with empty string not generated"


@pytest.mark.question_two_part_c
def test_rot13_encrypt():
    """Test the ROT13 encryption function."""
    assert rot13_encrypt("abc") == "nop", "Encrypt: Failed to shift lowercase letters"
    assert rot13_encrypt("ABC") == "NOP", "Encrypt: Failed to shift uppercase letters"
    assert rot13_encrypt("nop") == "abc", "Encrypt: Failed to wrap around lowercase letters"
    assert rot13_encrypt("NOP") == "ABC", "Encrypt: Failed to wrap around uppercase letters"
    assert rot13_encrypt("AbC") == "NoP", "Encrypt: Failed to handle mixed case letters"
    assert rot13_encrypt("123") == "123", "Encrypt: Failed to ignore non-alphabetic characters of numbers"
    assert rot13_encrypt("%$#") == "%$#", "Encrypt: Failed to ignore non-alphabetic characters of punctuation"


@pytest.mark.question_two_part_c
def test_rot13_decrypt():
    """Test the ROT13 decryption function."""
    assert rot13_decrypt("nop") == "abc", "Decrypt: Failed to shift lowercase letters"
    assert rot13_decrypt("NOP") == "ABC", "Decrypt: Failed to shift uppercase letters"
    assert rot13_decrypt("abc") == "nop", "Decrypt: Failed to wrap around lowercase letters"
    assert rot13_decrypt("ABC") == "NOP", "Decrypt: Failed to wrap around uppercase letters"
    assert rot13_decrypt("NoP") == "AbC", "Decrypt: Failed to handle mixed case letters"
    assert rot13_decrypt("123") == "123", "Decrypt: Failed to ignore non-alphabetic characters of numbers"
    assert rot13_decrypt("%$#") == "%$#", "Decrypt: Failed to ignore non-alphabetic characters of punctuation"
