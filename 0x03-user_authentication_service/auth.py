#!/usr/bin/env python3
"""
This module contains methods that handle authentication
"""
import bcrypt
from db import DB


def _hash_password(password: str) -> bytes:
    """Generate a salted hash of the input password
    """
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """
    Class to handle all authentication
    """
    def register_user(self, email, password):
        """
        Registers a new user
        """
        # Check if the user already exists
        if self._db.get_user_by_email(email) is not None:
            raise ValueError("User {} already exists".format(email))

        # Hash the password
        hashed_password = self._hash_password(password)

        # Create a new User object and save it
        user = User(email, hashed_password
        self._db.save_user(user)

        return user

