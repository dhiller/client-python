# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1VirtualMachineSnapshotCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'message': 'str',
        'reason': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'message': 'message',
        'reason': 'reason',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, message=None, reason=None, status=None, type=None):
        """
        V1alpha1VirtualMachineSnapshotCondition - a model defined in Swagger
        """

        self._message = None
        self._reason = None
        self._status = None
        self._type = None

        if message is not None:
          self.message = message
        if reason is not None:
          self.reason = reason
        self.status = status
        self.type = type

    @property
    def message(self):
        """
        Gets the message of this V1alpha1VirtualMachineSnapshotCondition.

        :return: The message of this V1alpha1VirtualMachineSnapshotCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1alpha1VirtualMachineSnapshotCondition.

        :param message: The message of this V1alpha1VirtualMachineSnapshotCondition.
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this V1alpha1VirtualMachineSnapshotCondition.

        :return: The reason of this V1alpha1VirtualMachineSnapshotCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1alpha1VirtualMachineSnapshotCondition.

        :param reason: The reason of this V1alpha1VirtualMachineSnapshotCondition.
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """
        Gets the status of this V1alpha1VirtualMachineSnapshotCondition.

        :return: The status of this V1alpha1VirtualMachineSnapshotCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1alpha1VirtualMachineSnapshotCondition.

        :param status: The status of this V1alpha1VirtualMachineSnapshotCondition.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def type(self):
        """
        Gets the type of this V1alpha1VirtualMachineSnapshotCondition.

        :return: The type of this V1alpha1VirtualMachineSnapshotCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1alpha1VirtualMachineSnapshotCondition.

        :param type: The type of this V1alpha1VirtualMachineSnapshotCondition.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1VirtualMachineSnapshotCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
