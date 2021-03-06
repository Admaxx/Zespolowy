# coding: utf-8

"""
    SimpleCalc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Input(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'a': 'float',
        'b': 'float',
        'op': 'str'
    }

    attribute_map = {
        'a': 'a',
        'b': 'b',
        'op': 'op'
    }

    def __init__(self, a=None, b=None, op=None):  # noqa: E501
        """Input - a model defined in Swagger"""  # noqa: E501

        self._a = None
        self._b = None
        self._op = None
        self.discriminator = None

        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if op is not None:
            self.op = op

    @property
    def a(self):
        """Gets the a of this Input.  # noqa: E501


        :return: The a of this Input.  # noqa: E501
        :rtype: float
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this Input.


        :param a: The a of this Input.  # noqa: E501
        :type: float
        """

        self._a = a

    @property
    def b(self):
        """Gets the b of this Input.  # noqa: E501


        :return: The b of this Input.  # noqa: E501
        :rtype: float
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this Input.


        :param b: The b of this Input.  # noqa: E501
        :type: float
        """

        self._b = b

    @property
    def op(self):
        """Gets the op of this Input.  # noqa: E501


        :return: The op of this Input.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this Input.


        :param op: The op of this Input.  # noqa: E501
        :type: str
        """

        self._op = op

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Input, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Input):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
