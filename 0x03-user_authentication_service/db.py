#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Creates a user on db
        """
        addUser = User(email=email, hashed_password=hashed_password)
        self._session.add(addUser)
        self._session.commit()
        return addUser

    def find_user_by(self, **kwargs):
        """ind a user based on filter queries
        """
        if not kwargs:
            raise InvalidRequestError

        cols = ["id", "email", "hashed_password", "session_id", "reset_token"]

        for arg in kwargs:
            if arg not in cols:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()
        if user:
            return user
        else:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes in the database
        """
        user = self.find_user_by(id=user_id)
        cols = ["email", "hashed_password", "session_id", "reset_token"]
        for arg in kwargs:
            if arg not in cols:
                raise ValueError(f"Invalid attribute: {arg}")
            setattr(user, arg, kwargs[arg])
        self._session.commit()
