import pytest
from project import check_strength, generate_password, save_password, load_passwords

def test_check_strength():
    assert check_strength("abc") == (
        "longer than 8 characters ❌\n"
        "No uppercase ❌\n"
        "Contains lowercase ✔️\n"
        "No digit ❌\n"
        "No symbol ❌\n"
        "Total score: 20 (weak)"
    )

    assert check_strength("abcABC123") == (
        "longer than 8 characters ✔️\n"
        "Contains uppercase ✔️\n"
        "Contains lowercase ✔️\n"
        "Contains digit ✔️\n"
        "No symbol ❌\n"
        "Total score: 80 (medium)"
    )

    assert check_strength("Hello, world") == (
        "longer than 8 characters ✔️\n"
        "Contains uppercase ✔️\n"
        "Contains lowercase ✔️\n"
        "No digit ❌\n"
        "Contains symbol ✔️\n"
        "Total score: 80 (medium)"
    )

def test_generate_password():
    password = generate_password(20)
    assert len(password) == 20
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isdigit() for char in password)


def test_save_password(tmp_path):
    file = tmp_path / "passwords.txt"
    keyfile = tmp_path / "keys.txt"

    assert save_password("mypassword123!", filename=file, keyfile=keyfile) == "Password saved successfully!"


def test_load_passwords(tmp_path):
    file = tmp_path / "passwords.txt"
    keyfile = tmp_path / "keys.txt"

    save_password("mypassword123!", filename=file, keyfile=keyfile)

    assert "mypassword123!" in load_passwords(filename=file, keyfile=keyfile)