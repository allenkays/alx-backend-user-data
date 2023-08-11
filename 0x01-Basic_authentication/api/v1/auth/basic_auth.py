#!/usr/bin/env python3
"""
Basic authentication implementation
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Subclass of Auth
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
    )-> str:
        """
        Method to extract base64 encoded authorization from the header
        """
        if (authorization_header is None):
            return None
        elif not (isinstance(authorization_header, str)):
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        else:
            base64_cred = authorization_header.split(" ")[1]
            return base64_cred
