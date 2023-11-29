from .smart_device import SmartDevice
import datetime

class Thermostat(SmartDevice):
    """
    A class representing a thermostat, which is a type of smart device.

    Attributes:
        temperature (int): The current temperature setting of the thermostat.
        __device_type (str): The type of the device, in this case "Thermostat".
    """

    def __init__(self, device_id):
        """
        The constructor for the Thermostat class.

        Parameters:
            device_id (str): The ID of the device.
        """
        super().__init__(device_id)
        self.temperature = 22
        self.__device_type = "Thermostat"

    def set_temperature(self, temp):
        """
        Sets the temperature of the thermostat.

        Parameters:
            temp (int): The desired temperature.

        Raises:
            ValueError: If temp is not between 0 and 40.
        """
        if temp > 40 or temp < 0:
            raise ValueError("Temperature cannot be more than 40 or less than 0")
        else:
            if temp > 0:
                self.turn_on()
                self.temperature = temp
            else:
                self.turn_off()
                self.temperature = temp

    @property
    def device_type(self):
        """
        The device_type property.

        Returns:
            str: The type of the device, in this case "Thermostat".
        """
        return self.__device_type

    def get_data(self):
        """
        Returns a string with the current time, device ID, status, and temperature.

        Returns:
            str: A string with the current time, device ID, status, and temperature.
        """
        return f"time: {datetime.datetime.now().isoformat()} device_id: {self.id} status: {self.status}  temperature: {self.temperature}"

    def __str__(self):
        """
        Returns a string representation of the Thermostat object.

        Returns:
            str: A string representation of the Thermostat object.
        """
        return f"Device: Thermostat Device Id: {self.id} Temperature: {self.temperature} Status: {self.status}"
