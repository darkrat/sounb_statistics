# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, patronymic_name: str=None, first_name: str=None, last_name: str=None, username: str=None, email: str=None, password: str=None, phone: str=None, user_status: int=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param patronymic_name: The patronymic_name of this User.  # noqa: E501
        :type patronymic_name: str
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param phone: The phone of this User.  # noqa: E501
        :type phone: str
        :param user_status: The user_status of this User.  # noqa: E501
        :type user_status: int
        """
        self.swagger_types = {
            'id': int,
            'patronymic_name': str,
            'first_name': str,
            'last_name': str,
            'username': str,
            'email': str,
            'password': str,
            'phone': str,
            'user_status': int
        }

        self.attribute_map = {
            'id': 'id',
            'patronymic_name': 'patronymicName',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'username': 'username',
            'email': 'email',
            'password': 'password',
            'phone': 'phone',
            'user_status': 'userStatus'
        }

        self._id = id
        self._patronymic_name = patronymic_name
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._email = email
        self._password = password
        self._phone = phone
        self._user_status = user_status

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """

        self._id = id

    @property
    def patronymic_name(self) -> str:
        """Gets the patronymic_name of this User.


        :return: The patronymic_name of this User.
        :rtype: str
        """
        return self._patronymic_name

    @patronymic_name.setter
    def patronymic_name(self, patronymic_name: str):
        """Sets the patronymic_name of this User.


        :param patronymic_name: The patronymic_name of this User.
        :type patronymic_name: str
        """

        self._patronymic_name = patronymic_name

    @property
    def first_name(self) -> str:
        """Gets the first_name of this User.


        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this User.


        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """

        self._password = password

    @property
    def phone(self) -> str:
        """Gets the phone of this User.


        :return: The phone of this User.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this User.


        :param phone: The phone of this User.
        :type phone: str
        """

        self._phone = phone

    @property
    def user_status(self) -> int:
        """Gets the user_status of this User.

        User Status  # noqa: E501

        :return: The user_status of this User.
        :rtype: int
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status: int):
        """Sets the user_status of this User.

        User Status  # noqa: E501

        :param user_status: The user_status of this User.
        :type user_status: int
        """

        self._user_status = user_status
