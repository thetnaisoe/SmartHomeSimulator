import random
import datetime
import tkinter as tk

from src.devices.smart_device import SmartDevice
from src.devices.smart_light import SmartLight
from src.devices.thermostat import Thermostat
from src.devices.security_camera import SecurityCamera
from src.automation_system import AutomationSystem

class SmartHomeSimulator(tk.Tk):
    """
    A class representing a smart home simulator, which is a GUI application for simulating a smart home.

    Attributes:
        devices_status_text (tk.Text): A text widget for displaying the status of the devices.
        smart_light (SmartLight): A SmartLight object representing a smart light.
        thermostat (Thermostat): A Thermostat object representing a thermostat.
        security_camera (SecurityCamera): A SecurityCamera object representing a security camera.
        smart_light_status_var (tk.StringVar): A StringVar object for storing the status of the smart light.
        thermostat_status_var (tk.StringVar): A StringVar object for storing the status of the thermostat.
        security_camera_var (tk.StringVar): A StringVar object for storing the status of the security camera.
    """
    def __init__(self):
        """
        The constructor for the SmartHomeSimulator class.
        """
        super().__init__()

        self.title("Smart Home IoT Simulator")
        self.geometry("800x800")
        self.configure(bg="grey")

        title_label = tk.Label(
            self,
            text="Smart Home IoT Simulator",
            font=("Helvetica", 18, "bold"),
            fg="black",
            bg="grey",
        )
        title_label.pack(pady=20)

        self.devices_status_text = tk.Text(self, height=7, width=100)
        self.devices_status_text.pack(side="top")

        self.smart_light = SmartLight("Living Room Light")
        self.thermostat = Thermostat("Living Room Thermostat")
        self.security_camera = SecurityCamera("Front Door Camera")

        self.smart_light_status_var = tk.StringVar()
        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")

        self.thermostat_status_var = tk.StringVar()
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")

        self.security_camera_var = tk.StringVar()
        self.security_camera_var.set(f"Security Camera Status: {self.security_camera.status}")

        self.display_current_devices()

        living_room_brightness_label = tk.Label(
            self,
            text="Living Room Light Brightness",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
        )
        living_room_brightness_label.pack(pady=5, side="top")

        self.brightness_level_label = tk.Label(
            self,
            text="Living Room Light: 0",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
        )
        self.brightness_level_label.pack(pady=5, side="top")

        self.brightness_scale = tk.Scale(
            self,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            length=200,
            sliderlength=15,
            command=self.update_brightness,
        )
        self.brightness_scale.pack(pady=10)

        toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
            command=self.toggle_smart_light,
        )
        toggle_button.pack(pady=10)

        thermostat_temperature_label = tk.Label(
            self,
            text="Living Room Thermostat Temperature",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
        )
        thermostat_temperature_label.pack(pady=5, side="top")

        self.temperature_level_label = tk.Label(
            self,
            text="Living Room Thermostat: 0",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
        )
        self.temperature_level_label.pack(pady=5, side="top")

        self.temperature_scale = tk.Scale(
            self,
            from_=0,
            to=40,
            orient=tk.HORIZONTAL,
            length=200,
            sliderlength=15,
            command=self.update_temperature,
        )
        self.temperature_scale.pack(pady=10)

        thermostat_toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
            command=self.toggle_thermostat,
        )
        thermostat_toggle_button.pack(pady=10)

        security_camera_status_label = tk.Label(
            self,
            text="Front Door Camera Motion Detection",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
        )
        security_camera_status_label.pack(pady=5, side="top")

        self.motion_status_label = tk.Label(
            self,
            text="Front Door Camera Motion Status: No motion",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
        )
        self.motion_status_label.pack(pady=5, side="top")

        motion_button = tk.Button(
            self,
            text="Random Detect Motion",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
            command=self.toggle_motion,
        )
        motion_button.pack(pady=10)

        security_camera_toggle_button = tk.Button(
            self,
            text="Toggle On/Off",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
            command=self.toggle_security_camera,
        )
        security_camera_toggle_button.pack(pady=10)

        self.automation_rule_var = tk.Label(
            self,
            text="Automation Rule: Turn on lights when motion is detected",
            font=("Helvetica", 14, "bold"),
            fg="black",
            bg="grey",
        )
        self.automation_rule_var.pack(pady=5, side="top")

    def update_brightness(self, value):
        """
        Updates the brightness of the smart light.

        Parameters:
            value (str): The new brightness value.
        """
        self.smart_light.adjust_brightness(int(value))
        self.brightness_level_label["text"] = f"Brightness Level: {value}"
        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")
        self.update_status_textarea()
        

    def toggle_smart_light(self):
        """
        Toggles the smart light on or off.
        """
        if self.smart_light.status == "on":
            self.smart_light.turn_off()
            self.smart_light.adjust_brightness(0)
        else:
            self.smart_light.turn_on()

        self.smart_light_status_var.set(f"SmartLight Status: {self.smart_light.status}")
        self.brightness_scale.set(self.smart_light.brightness)
        self.update_status_textarea()


    def update_temperature(self, value):
        """
        Updates the temperature of the thermostat.

        Parameters:
            value (str): The new temperature value.
        """
        self.thermostat.set_temperature(int(value))
        self.temperature_level_label["text"] = f"Temperature Level: {value}"
        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")
        self.update_status_textarea()
     

    def toggle_thermostat(self):
        """
        Toggles the thermostat on or off.
        """
        if self.thermostat.status == "on":
            self.thermostat.turn_off()
            self.thermostat.set_temperature(0)
        else:
            self.thermostat.turn_on()

        self.thermostat_status_var.set(f"Thermostat Status: {self.thermostat.status}")
        self.temperature_scale.set(self.thermostat.temperature)
        self.update_status_textarea()
     

    def toggle_security_camera(self):
        """
        Toggles the security camera on or off.
        """
        if self.security_camera.status == "on":
            self.security_camera.turn_off()
            self.security_camera.set_security_status("No motion")
        else:
            self.security_camera.turn_on()

        self.security_camera_var.set(f"Security Camera Status: {self.security_camera.status}")
        self.update_status_textarea()
      

    def toggle_motion(self):
        """
        Toggles the motion detection status of the security camera.
        """
        status = random.choice(["Detected motion", "No motion"])
        self.security_camera.set_security_status(status)

        self.motion_status_label["text"] = f"Motion Status: {status}"
        self.update_status_textarea()
      

    def display_current_devices(self):
        """
        Displays the current status of all devices in the text widget.
        """
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat, self.security_camera]
        for device in devices:
            self.devices_status_text.insert(tk.END, f"{device.id}: {device.device_type} Status: {device.status}\n")

    def update_status_textarea(self):
        """
        Updates the text widget with the current status of all devices.
        """
        self.devices_status_text.delete(1.0, tk.END)
        devices = [self.smart_light, self.thermostat, self.security_camera]
        for device in devices:
            status_info = f"{device.id}: {device.device_type}    Status: {device.status}"

            if isinstance(device, SmartLight):
                status_info += f"    Brightness: {device.brightness}"
            elif isinstance(device, Thermostat):
                status_info += f"    Temperature: {device.temperature}"
            elif isinstance(device, SecurityCamera):
                status_info += f"    Security Status: {device.get_security_status()}"

            self.devices_status_text.insert(tk.END, status_info + "\n")

"""
root = SmartHomeSimulator()
root.mainloop()
This is how we can run the program

"""

root = SmartHomeSimulator()
root.mainloop()