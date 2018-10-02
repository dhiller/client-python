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


class V1DomainSpec(object):
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
        'clock': 'V1Clock',
        'cpu': 'V1CPU',
        'devices': 'V1Devices',
        'features': 'V1Features',
        'firmware': 'V1Firmware',
        'io_threads_policy': 'V1IOThreadsPolicy',
        'machine': 'V1Machine',
        'memory': 'V1Memory',
        'resources': 'V1ResourceRequirements'
    }

    attribute_map = {
        'clock': 'clock',
        'cpu': 'cpu',
        'devices': 'devices',
        'features': 'features',
        'firmware': 'firmware',
        'io_threads_policy': 'ioThreadsPolicy',
        'machine': 'machine',
        'memory': 'memory',
        'resources': 'resources'
    }

    def __init__(self, clock=None, cpu=None, devices=None, features=None, firmware=None, io_threads_policy=None, machine=None, memory=None, resources=None):
        """
        V1DomainSpec - a model defined in Swagger
        """

        self._clock = None
        self._cpu = None
        self._devices = None
        self._features = None
        self._firmware = None
        self._io_threads_policy = None
        self._machine = None
        self._memory = None
        self._resources = None

        if clock is not None:
          self.clock = clock
        if cpu is not None:
          self.cpu = cpu
        self.devices = devices
        if features is not None:
          self.features = features
        if firmware is not None:
          self.firmware = firmware
        if io_threads_policy is not None:
          self.io_threads_policy = io_threads_policy
        if machine is not None:
          self.machine = machine
        if memory is not None:
          self.memory = memory
        if resources is not None:
          self.resources = resources

    @property
    def clock(self):
        """
        Gets the clock of this V1DomainSpec.
        Clock sets the clock and timers of the vmi. +optional

        :return: The clock of this V1DomainSpec.
        :rtype: V1Clock
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """
        Sets the clock of this V1DomainSpec.
        Clock sets the clock and timers of the vmi. +optional

        :param clock: The clock of this V1DomainSpec.
        :type: V1Clock
        """

        self._clock = clock

    @property
    def cpu(self):
        """
        Gets the cpu of this V1DomainSpec.
        CPU allow specified the detailed CPU topology inside the vmi. +optional

        :return: The cpu of this V1DomainSpec.
        :rtype: V1CPU
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this V1DomainSpec.
        CPU allow specified the detailed CPU topology inside the vmi. +optional

        :param cpu: The cpu of this V1DomainSpec.
        :type: V1CPU
        """

        self._cpu = cpu

    @property
    def devices(self):
        """
        Gets the devices of this V1DomainSpec.
        Devices allows adding disks, network interfaces, ...

        :return: The devices of this V1DomainSpec.
        :rtype: V1Devices
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """
        Sets the devices of this V1DomainSpec.
        Devices allows adding disks, network interfaces, ...

        :param devices: The devices of this V1DomainSpec.
        :type: V1Devices
        """
        if devices is None:
            raise ValueError("Invalid value for `devices`, must not be `None`")

        self._devices = devices

    @property
    def features(self):
        """
        Gets the features of this V1DomainSpec.
        Features like acpi, apic, hyperv. +optional

        :return: The features of this V1DomainSpec.
        :rtype: V1Features
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this V1DomainSpec.
        Features like acpi, apic, hyperv. +optional

        :param features: The features of this V1DomainSpec.
        :type: V1Features
        """

        self._features = features

    @property
    def firmware(self):
        """
        Gets the firmware of this V1DomainSpec.
        Firmware. +optional

        :return: The firmware of this V1DomainSpec.
        :rtype: V1Firmware
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this V1DomainSpec.
        Firmware. +optional

        :param firmware: The firmware of this V1DomainSpec.
        :type: V1Firmware
        """

        self._firmware = firmware

    @property
    def io_threads_policy(self):
        """
        Gets the io_threads_policy of this V1DomainSpec.
        Controls whether or not disks will share IOThreads. Omitting IOThreadsPolicy disables use of IOThreads. One of: shared, auto +optional

        :return: The io_threads_policy of this V1DomainSpec.
        :rtype: V1IOThreadsPolicy
        """
        return self._io_threads_policy

    @io_threads_policy.setter
    def io_threads_policy(self, io_threads_policy):
        """
        Sets the io_threads_policy of this V1DomainSpec.
        Controls whether or not disks will share IOThreads. Omitting IOThreadsPolicy disables use of IOThreads. One of: shared, auto +optional

        :param io_threads_policy: The io_threads_policy of this V1DomainSpec.
        :type: V1IOThreadsPolicy
        """

        self._io_threads_policy = io_threads_policy

    @property
    def machine(self):
        """
        Gets the machine of this V1DomainSpec.
        Machine type. +optional

        :return: The machine of this V1DomainSpec.
        :rtype: V1Machine
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """
        Sets the machine of this V1DomainSpec.
        Machine type. +optional

        :param machine: The machine of this V1DomainSpec.
        :type: V1Machine
        """

        self._machine = machine

    @property
    def memory(self):
        """
        Gets the memory of this V1DomainSpec.
        Memory allow specifying the VMI memory features. +optional

        :return: The memory of this V1DomainSpec.
        :rtype: V1Memory
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this V1DomainSpec.
        Memory allow specifying the VMI memory features. +optional

        :param memory: The memory of this V1DomainSpec.
        :type: V1Memory
        """

        self._memory = memory

    @property
    def resources(self):
        """
        Gets the resources of this V1DomainSpec.
        Resources describes the Compute Resources required by this vmi.

        :return: The resources of this V1DomainSpec.
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1DomainSpec.
        Resources describes the Compute Resources required by this vmi.

        :param resources: The resources of this V1DomainSpec.
        :type: V1ResourceRequirements
        """

        self._resources = resources

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
        if not isinstance(other, V1DomainSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
