import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import User
from hashing import hash_password
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/fastapi_db")

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_user(db):
    user = User(
        username="testuser",
        email="testuser@example.com",
        password_hash=hash_password("password123")
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    assert user.id is not None
    assert user.username == "testuser"

def test_duplicate_username(db):
    user1 = User(
        username="dupuser",
        email="dup1@example.com",
        password_hash=hash_password("password123")
    )
    db.add(user1)
    db.commit()

    user2 = User(
        username="dupuser",
        email="dup2@example.com",
        password_hash=hash_password("password123")
    )
    db.add(user2)
    with pytest.raises(Exception):
        db.commit()

def test_duplicate_email(db):
    db.rollback()
    user1 = User(
        username="emailuser1",
        email="same@example.com",
        password_hash=hash_password("password123")
    )
    db.add(user1)
    db.commit()

    user2 = User(
        username="emailuser2",
        email="same@example.com",
        password_hash=hash_password("password123")
    )
    db.add(user2)
    with pytest.raises(Exception):
        db.commit()