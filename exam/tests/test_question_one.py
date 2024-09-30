"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    decrypt_caesar_cipher,
    encrypt_caesar_cipher,
    generate_fuzzer_value,
    reverse_string_decrypt,
    reverse_string_encrypt,
    reverse_string_encrypt_dictionary,
)


@pytest.mark.question_one_part_a
def test_encrypt_caesar_cipher():
    """Confirm correctness of question part."""
    assert encrypt_caesar_cipher("ABC", 3) == "DEF", "Failed to shift uppercase letters"
    assert encrypt_caesar_cipher("abc", 3) == "def", "Failed to shift lowercase letters"
    assert (
        encrypt_caesar_cipher("XYZ", 3) == "ABC"
    ), "Failed to wrap around uppercase letters"
    assert (
        encrypt_caesar_cipher("xyz", 3) == "abc"
    ), "Failed to wrap around lowercase letters"
    assert (
        encrypt_caesar_cipher("AbC", 3) == "DeF"
    ), "Failed to handle mixed case letters"
    assert (
        encrypt_caesar_cipher("AbC", 3) == "DeF"
    ), "Failed to handle mixed case letters with symbols"


@pytest.mark.question_one_part_a
def test_decrypt_caesar_cipher():
    """Confirm correctness of question part."""
    assert decrypt_caesar_cipher("DEF", 3) == "ABC", "Failed to shift uppercase letters"
    assert decrypt_caesar_cipher("def", 3) == "abc", "Failed to shift lowercase letters"
    assert (
        decrypt_caesar_cipher("ABC", 3) == "XYZ"
    ), "Failed to wrap around uppercase letters"
    assert (
        decrypt_caesar_cipher("abc", 3) == "xyz"
    ), "Failed to wrap around lowercase letters"
    assert (
        decrypt_caesar_cipher("DeF", 3) == "AbC"
    ), "Failed to handle mixed case letters"


@pytest.mark.question_one_part_b
def test_generate_fuzzer_values():
    """Confirm correctness of question part."""
    max_length = 10
    result = generate_fuzzer_value(max_length)
    assert len(result) <= max_length, "Generated string is too long"
    char_start = 65
    char_range = 26
    result = generate_fuzzer_value(100, char_start, char_range)
    for char in result:
        assert (
            char_start <= ord(char) < char_start + char_range
        ), "Character is not in range"
    result = generate_fuzzer_value(0)
    assert result == "", "Empty string not generated"


@pytest.mark.question_one_part_c
def test_reverse_string_encrypt():
    """Confirm correctness of question part."""
    assert reverse_string_encrypt("ABC") == "CBA", "Failed to reverse string"
    assert reverse_string_encrypt("123") == "321", "Failed to reverse numeric string"
    assert reverse_string_encrypt("abc") == "cba", "Failed to reverse lowercase string"
    assert reverse_string_encrypt("AbC") == "CbA", "Failed to reverse mixed case string"
    assert reverse_string_encrypt("X") == "X", "Failed to handle singleton string"
    assert reverse_string_encrypt("") == "", "Failed to handle empty string"


@pytest.mark.question_one_part_c
def test_reverse_string_decrypt():
    """Confirm correctness of question part."""
    assert reverse_string_decrypt("CBA") == "ABC", "Failed to reverse string"
    assert reverse_string_decrypt("321") == "123", "Failed to reverse numeric string"
    assert reverse_string_decrypt("cba") == "abc", "Failed to reverse lowercase string"
    assert reverse_string_decrypt("CbA") == "AbC", "Failed to reverse mixed case string"
    assert reverse_string_decrypt("X") == "X", "Failed to handle singleton string"
    assert reverse_string_decrypt("") == "", "Failed to handle empty string"


def test_reverse_string_encrypt_dictionary():
    """Confirm correctness of question part."""
    assert reverse_string_encrypt_dictionary(["ABC", "123", "abc", "AbC", "X", ""]) == {
        "ABC": "CBA",
        "123": "321",
        "abc": "cba",
        "AbC": "CbA",
        "X": "X",
        "": "",
    }, "Failed to encrypt and map plaintexts to ciphertexts"
