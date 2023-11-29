from .smart_device import SmartDevice

class SmartLight(SmartDevice):
    """
    A class representing a smart light, which is a type of smart device.

    Attributes:
        __brightness (int): The current brightness level of the smart light.
        __device_type (str): The type of the device, in this case "SmartLight".
    """

    def __init__(self, device_id):
        """
        The constructor for the SmartLight class.

        Parameters:
            device_id (str): The ID of the device.
        """
        super().__init__(device_id)
        self.__brightness = 0
        self.__device_type = "SmartLight"

    @property
    def brightness(self):
        """
        The brightness property.

        Returns:
            int: The current brightness level of the smart light.
        """
        return self.__brightness

    @property
    def device_type(self):
        """
        The device_type property.

        Returns:
            str: The type of the device, in this case "SmartLight".
        """
        return self.__device_type

    def adjust_brightness(self, brightness: int):
        """
        Adjusts the brightness of the smart light.

        Parameters:
            brightness (int): The desired brightness level.

        Raises:
            ValueError: If brightness is not between 0 and 100.
        """
        if brightness > 100 or brightness < 0:
            raise ValueError(
                "Brightness level cannot be more than 100 or less than 0"
            )
        if brightness > 0:
            self.turn_on()
        self.__brightness = brightness
        if brightness == 0:
            self.turn_off()

    def __str__(self) -> str:
        """
        Returns a string representation of the SmartLight object.

        Returns:
            str: A string representation of the SmartLight object.
        """
        return f"Device: Smart Light Device Id: {self.id} Brightness: {self.brightness} Status: {self.status}"
    
    