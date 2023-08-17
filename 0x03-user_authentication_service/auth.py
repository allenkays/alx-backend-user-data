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
        try:
            self._db.find_user_by(email=email):
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))
