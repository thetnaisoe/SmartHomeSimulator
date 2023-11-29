import datetime
from .smart_device import SmartDevice

class SecurityCamera(SmartDevice):
    """
    A class representing a security camera, which is a type of smart device.

    Attributes:
        __securityStatus (str): The current security status of the camera.
        __device_type (str): The type of the device, in this case "SecurityCamera".
    """

    def __init__(self, device_id: str):
        """
        The constructor for the SecurityCamera class.

        Parameters:
            device_id (str): The ID of the device.
        """
        super().__init__(device_id)
        self.__securityStatus = "No motion"
        self.__device_type = "SecurityCamera"

    @property
    def device_type(self):
        """
        The device_type property.

        Returns:
            str: The type of the device, in this case "SecurityCamera".
        """
        return self.__device_type

    def get_security_status(self):
        """
        Returns the current security status of the camera.

        Returns:
            str: The current security status of the camera.
        """
        return self.__securityStatus

    def set_security_status(self, status):
        """
        Sets the security status of the camera.

        Parameters:
            status (str): The desired security status.
        """
        self.__securityStatus = status

    def get_data(self):
        """
        Returns a string with the current time, device ID, status, and security status.

        Returns:
            str: A string with the current time, device ID, status, and security status.
        """
        return f"time: {datetime.datetime.now().isoformat()} device_id: {self.id} status: {self.status} security_status: {self.get_security_status()}"

    def __str__(self):
        """
        Returns a string representation of the SecurityCamera object.

        Returns:
            str: A string representation of the SecurityCamera object.
        """
        return f"Device: Security Camera Device Id: {self.id} Security Status: {self.__securityStatus} Status: {self.status}"