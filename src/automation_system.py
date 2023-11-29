import random
from src.devices.security_camera import SecurityCamera
from src.devices.smart_device import SmartDevice
from src.devices.smart_light import SmartLight
from src.devices.thermostat import Thermostat

class AutomationSystem:
    """
    A class representing an automation system, which manages multiple smart devices.

    Attributes:
        cameras (list): A list of SecurityCamera objects.
        thermostats (list): A list of Thermostat objects.
        lights (list): A list of SmartLight objects.
    """

    def __init__(self):
        """
        The constructor for the AutomationSystem class.
        """
        self.cameras = []
        self.thermostats = []
        self.lights = []

    def discover_devices(self):
        """
        Discovers devices. This method is currently not implemented.
        """
        pass

    def add_device(self, device: SmartDevice):
        """
        Adds a device to the automation system.

        Parameters:
            device (SmartDevice): The device to add.
        """
        if isinstance(device, SecurityCamera):
            self.cameras.append(device)
        elif isinstance(device, Thermostat):
            self.thermostats.append(device)
        elif isinstance(device, SmartLight):
            self.lights.append(device)

    def turn_lights_automatically(self, camera_id):
        """
        Turns lights on or off automatically based on the security status of a camera.

        Parameters:
            camera_id (str): The ID of the camera to check.
        """
        for camera in self.cameras:
            if camera.id() == camera_id:
                if camera.get_security_status() == "Detected motion":
                    for light_bulb in self.lights:
                        light_bulb.turn_on()
                else:
                    for light_bulb in self.lights:
                        light_bulb.turn_off()

    def randomization(self):
        """
        Randomizes the settings of all devices in the automation system.
        """
        for dev in self.lights + self.cameras + self.thermostats:
            if isinstance(dev, SmartLight):
                brightness = random.randint(0, 100)
                dev.adjust_brightness(brightness)
            elif isinstance(dev, Thermostat):
                temp = random.randint(0, 100)
                dev.set_temperature(temp)
            elif isinstance(dev, SecurityCamera):
                status = random.choice(["Motion Detected", "No Motion Detected"])
                dev.set_security_status(status)
