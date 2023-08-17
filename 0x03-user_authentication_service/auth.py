#!/usr/bin/env python3
"""
This module contains methods that handle authentication
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Generate a salted hash of the input password
    """
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
