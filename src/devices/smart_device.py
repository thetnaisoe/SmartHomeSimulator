class SmartDevice:
    """
    A class representing a generic smart device.

    Attributes:
        __device_id (str): The ID of the device.
        __status (str): The status of the device, either "on" or "off".
    """

    def __init__(self, device_id: str):
        """
        The constructor for the SmartDevice class.

        Parameters:
            device_id (str): The ID of the device.
        """
        self.__device_id = device_id
        self.__status = "off"

    @property
    def status(self):
        """
        The status property.

        Returns:
            str: The status of the device, either "on" or "off".
        """
        return self.__status

    @property
    def id(self):
        """
        The id property.

        Returns:
            str: The ID of the device.
        """
        return self.__device_id

    def turn_on(self):
        """
        Turns on the device if it's currently off.
        """
        if self.__status == "off":
            self.__status = "on"

    def turn_off(self):
        """
        Turns off the device if it's currently on.
        """
        if self.__status == "on":
            self.__status = "off"