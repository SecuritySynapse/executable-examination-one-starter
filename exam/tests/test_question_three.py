"""Confirm the correctness of functions in question_two."""

import pytest

# ruff: noqa: PLR2004
from questions.question_three import (
    count_spaces_and_newlines_cryptanalysis,
    count_words_cryptanalysis,
    decrypt_transposition_cipher,
    encrypt_transposition_cipher,
)


@pytest.mark.question_three_part_a
def test_encrypt_transposition_cipher():
    """Test for a question part."""
    assert (
        encrypt_transposition_cipher(8, "Common sense is not so common.")
        == "Cenoonommstmme oo snnio. s s c"
    ), "Encryption failed for key 8 and the common sense message"


@pytest.mark.question_three_part_a
def test_decrypt_transposition_cipher():
    """Test for a question part."""
    assert (
        decrypt_transposition_cipher(8, "Cenoonommstmme oo snnio. s s c")
        == "Common sense is not so common."
    ), "Decryption failed for key 8 and the common sense message"


@pytest.mark.question_three_part_b
def test_count_words_cryptanalysis():
    """Test for a question part."""
    assert count_words_cryptanalysis("hello hello world") == {
        "hello": 2,
        "world": 1,
    }, "Word count failed for string with one duplicated word"
    assert count_words_cryptanalysis("Python Python Python") == {
        "Python": 3
    }, "Word count failed for string with the same word"
    assert count_words_cryptanalysis("") == {}, "Word count failed for an empty string"
    assert count_words_cryptanalysis("Hello % extraction point") == {
        "Hello": 1,
        "%": 1,
        "extraction": 1,
        "point": 1,
    }, "Word count failed for string with a percent sign symbol and single-count words"
    assert count_words_cryptanalysis("^ % & @") == {
        "^": 1,
        "%": 1,
        "&": 1,
        "@": 1,
    }, "Word count failed for string with a numerous symbols"


@pytest.mark.question_three_part_c
def test_count_spaces_and_newlines_cryptanalysis():
    """Test for a question part."""
    assert count_spaces_and_newlines_cryptanalysis("hello world") == {
        "spaces": 1,
        "newlines": 0,
    }, "Count failed for 'hello world'"
    assert count_spaces_and_newlines_cryptanalysis("hello\nworld") == {
        "spaces": 0,
        "newlines": 1,
    }, "Count failed for 'hello\\nworld'"
    assert count_spaces_and_newlines_cryptanalysis("hello world\nPython") == {
        "spaces": 1,
        "newlines": 1,
    }, "Count failed for 'hello world\\nPython'"
    assert count_spaces_and_newlines_cryptanalysis("") == {
        "spaces": 0,
        "newlines": 0,
    }, "Count failed for an empty string"
