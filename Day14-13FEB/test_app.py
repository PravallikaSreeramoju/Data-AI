import pytest
from app import app, validate_input

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_valid_input():
    valid, message = validate_input("Anjali", "anjali@gmail.com", "22")
    assert valid is True
    assert message == "Registration successful"


def test_invalid_email():
    valid, message = validate_input("Anjali", "anjaligmail.com", "22")
    assert valid is False
    assert message == "Invalid email format"


def test_underage():
    valid, message = validate_input("Anjali", "anjali@gmail.com", "15")
    assert valid is False
    assert message == "Age must be 18 or above"


def test_empty_fields():
    valid, message = validate_input("", "anjali@gmail.com", "22")
    assert valid is False
    assert message == "All fields are required"