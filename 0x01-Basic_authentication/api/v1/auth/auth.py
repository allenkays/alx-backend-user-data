#!/usr/bin/env python3
"""
Class to manage api authentication
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Class methods to handle authentication requests
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method that manages queried paths

        Args:
            path (str): queried path
            excludeded_paths (list): list of paths that should not be queried

        Returns:
            False (bool): default return is false
            path (str): to be used later
            excluded_paths (list): to be used later
        """
        if path is None:
            return True
        if ((len(excluded_paths) == 0) or excluded_paths is None):
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        method to handle requests

        Args:
            requests (str): default is None for now

        Returns:
            None (str): returns none, request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Args:
            requests (str): defaults to none
        Returns:
            None (str): returns None, request will be the Flask request object
        """
        return None
