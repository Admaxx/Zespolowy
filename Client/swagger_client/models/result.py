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


class Result(object):
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
        'input': 'Input',
        'output': 'Output'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output'
    }

    def __init__(self, input=None, output=None):  # noqa: E501
        """Result - a model defined in Swagger"""  # noqa: E501

        self._input = None
        self._output = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if output is not None:
            self.output = output

    @property
    def input(self):
        """Gets the input of this Result.  # noqa: E501


        :return: The input of this Result.  # noqa: E501
        :rtype: Input
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this Result.


        :param input: The input of this Result.  # noqa: E501
        :type: Input
        """

        self._input = input

    @property
    def output(self):
        """Gets the output of this Result.  # noqa: E501


        :return: The output of this Result.  # noqa: E501
        :rtype: Output
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this Result.


        :param output: The output of this Result.  # noqa: E501
        :type: Output
        """

        self._output = output

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
        if issubclass(Result, dict):
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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
