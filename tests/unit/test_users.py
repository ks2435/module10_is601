from hashing import hash_password, verify_password
from schemas import UserCreate, UserRead
from datetime import datetime
import pytest

def test_hash_password():
    hashed = hash_password("mypassword")
    assert hashed != "mypassword"

def test_verify_password():
    hashed = hash_password("mypassword")
    assert verify_password("mypassword", hashed) == True

def test_verify_wrong_password():
    hashed = hash_password("mypassword")
    assert verify_password("wrongpassword", hashed) == False

def test_user_create_schema():
    user = UserCreate(username="alice", email="alice@example.com", password="secret123")
    assert user.username == "alice"
    assert user.email == "alice@example.com"

def test_user_create_invalid_email():
    with pytest.raises(Exception):
        UserCreate(username="alice", email="notanemail", password="secret123")

def test_user_read_schema():
    user = UserRead(id=1, username="alice", email="alice@example.com", created_at=datetime.now())
    assert user.id == 1
    assert user.username == "alice"