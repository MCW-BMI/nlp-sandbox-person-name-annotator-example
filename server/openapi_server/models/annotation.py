# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.entity import Entity
from openapi_server.models.user import User
from openapi_server import util

from openapi_server.models.entity import Entity  # noqa: E501
from openapi_server.models.user import User  # noqa: E501

class Annotation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, created_by=None, created_at=None, updated_by=None, updated_at=None, note_id=None, start=None, length=None, text=None):  # noqa: E501
        """Annotation - a model defined in OpenAPI

        :param id: The id of this Annotation.  # noqa: E501
        :type id: int
        :param created_by: The created_by of this Annotation.  # noqa: E501
        :type created_by: User
        :param created_at: The created_at of this Annotation.  # noqa: E501
        :type created_at: datetime
        :param updated_by: The updated_by of this Annotation.  # noqa: E501
        :type updated_by: User
        :param updated_at: The updated_at of this Annotation.  # noqa: E501
        :type updated_at: datetime
        :param note_id: The note_id of this Annotation.  # noqa: E501
        :type note_id: int
        :param start: The start of this Annotation.  # noqa: E501
        :type start: int
        :param length: The length of this Annotation.  # noqa: E501
        :type length: int
        :param text: The text of this Annotation.  # noqa: E501
        :type text: str
        """
        self.openapi_types = {
            'id': int,
            'created_by': User,
            'created_at': datetime,
            'updated_by': User,
            'updated_at': datetime,
            'note_id': int,
            'start': int,
            'length': int,
            'text': str
        }

        self.attribute_map = {
            'id': 'id',
            'created_by': 'createdBy',
            'created_at': 'createdAt',
            'updated_by': 'updatedBy',
            'updated_at': 'updatedAt',
            'note_id': 'noteId',
            'start': 'start',
            'length': 'length',
            'text': 'text'
        }

        self._id = id
        self._created_by = created_by
        self._created_at = created_at
        self._updated_by = updated_by
        self._updated_at = updated_at
        self._note_id = note_id
        self._start = start
        self._length = length
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'Annotation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Annotation of this Annotation.  # noqa: E501
        :rtype: Annotation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Annotation.

        ID  # noqa: E501

        :return: The id of this Annotation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Annotation.

        ID  # noqa: E501

        :param id: The id of this Annotation.
        :type id: int
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this Annotation.


        :return: The created_by of this Annotation.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Annotation.


        :param created_by: The created_by of this Annotation.
        :type created_by: User
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this Annotation.

        When the entity has been created  # noqa: E501

        :return: The created_at of this Annotation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Annotation.

        When the entity has been created  # noqa: E501

        :param created_at: The created_at of this Annotation.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_by(self):
        """Gets the updated_by of this Annotation.


        :return: The updated_by of this Annotation.
        :rtype: User
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Annotation.


        :param updated_by: The updated_by of this Annotation.
        :type updated_by: User
        """

        self._updated_by = updated_by

    @property
    def updated_at(self):
        """Gets the updated_at of this Annotation.

        When the entity has been updated  # noqa: E501

        :return: The updated_at of this Annotation.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Annotation.

        When the entity has been updated  # noqa: E501

        :param updated_at: The updated_at of this Annotation.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def note_id(self):
        """Gets the note_id of this Annotation.

        The note ID  # noqa: E501

        :return: The note_id of this Annotation.
        :rtype: int
        """
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        """Sets the note_id of this Annotation.

        The note ID  # noqa: E501

        :param note_id: The note_id of this Annotation.
        :type note_id: int
        """

        self._note_id = note_id

    @property
    def start(self):
        """Gets the start of this Annotation.

        The position of the first character  # noqa: E501

        :return: The start of this Annotation.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Annotation.

        The position of the first character  # noqa: E501

        :param start: The start of this Annotation.
        :type start: int
        """

        self._start = start

    @property
    def length(self):
        """Gets the length of this Annotation.

        The length of the annotation  # noqa: E501

        :return: The length of this Annotation.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Annotation.

        The length of the annotation  # noqa: E501

        :param length: The length of this Annotation.
        :type length: int
        """

        self._length = length

    @property
    def text(self):
        """Gets the text of this Annotation.

        The string annotated  # noqa: E501

        :return: The text of this Annotation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Annotation.

        The string annotated  # noqa: E501

        :param text: The text of this Annotation.
        :type text: str
        """

        self._text = text
