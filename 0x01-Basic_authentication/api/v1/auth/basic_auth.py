#!/usr/bin/env python3
"""
Basic authentication implementation
"""
from api.v1.auth.auth import AUTH


class BasicAuth(Auth):
    """
    Subclass of Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Method to extract base64 encoded authorization from the header
        """
        if authorization_header is none or not isinstance(authorization_header, str):
            return None
        if authorization_header.startsWith(Basic):
            return None
        # base64_cred = authorization_header.split(" ")[1]

        return authorization_header[len("Basic "):]
